use axum::extract::ConnectInfo;
use axum::response::sse::{Event, Sse};
use axum::response::IntoResponse;
use axum::response::Response;
use axum::{
    extract::{Query, State},
    http::StatusCode,
    response::Html,
    routing::{get, post},
    Json, Router,
};
use bb8::{Pool, PooledConnection};
use bb8_redis::bb8;
use bb8_redis::RedisConnectionManager;
use futures::stream::Stream;
use redis::AsyncCommands;
use serde_derive::{Deserialize, Serialize};
use serde_json::Value;
use std::collections::HashMap;
use std::{convert::Infallible, net::SocketAddr, time::Duration};
use tokio_stream::StreamExt as _;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

mod log;

use log::{Log, LogManager};

pub const DEFAULT_THREAD: &str = "k1";
// static import of the html file
const INDEX_HTML: &str = include_str!("../static/index.html");

type RedisConnectionPool = Pool<RedisConnectionManager>;
type ConnectionPool = DataConnector;

#[derive(Debug, Serialize, Deserialize, Default)]
struct InternalEntry {
    message: String,
    client_id: String,
}

#[derive(Clone)]
enum PoolKind {
    Redis(RedisConnectionPool),
    Internal(InternalPool),
}

#[derive(Clone)]
struct DataConnector {
    pool: PoolKind,
}

#[derive(Clone)]
struct InternalPool {
    pub logs: LogManager,
    pub kv: HashMap<String, String>,
}

impl Default for InternalPool {
    fn default() -> Self {
        InternalPool {
            logs: LogManager::new(),
            kv: HashMap::new(),
        }
    }
}

#[derive(Deserialize, Debug)]
struct Params {
    #[serde(default)]
    start: Option<String>,
    #[serde(default)]
    end: Option<String>,
    #[serde(default)]
    thread: Option<String>,
    #[serde(default)]
    identifier: Option<String>,
}

#[derive(Serialize, Deserialize)]
struct Message {
    message: String,
    client_id: String,
}

#[derive(Debug, Deserialize, Serialize)]
struct BaseMessage {
    room: String,
    message: String,
    score: i32,
}

#[derive(Debug, Deserialize, Serialize)]
#[serde(untagged)]
enum MyEnum {
    String(String),
    Value(Value),
}

pub async fn inner_main() {
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "unconscious_core=debug".into()),
        )
        .with(tracing_subscriber::fmt::layer())
        .init();

    let use_redis = std::env::var("UNCONSCIOUS_USE_REDIS").is_ok();

    let my_struct = if use_redis {
        tracing::debug!("connecting to redis");
        let redis_url =
            std::env::var("REDIS_URL").unwrap_or_else(|_| "redis://localhost".to_string());

        let manager = RedisConnectionManager::new(redis_url).unwrap();
        let pool = bb8::Pool::builder().build(manager).await.unwrap();

        // ping the database before starting
        let mut conn = pool.get().await.unwrap();
        conn.set::<&str, &str, ()>("foo", "bar").await.unwrap();
        let result: String = conn.get("foo").await.unwrap();
        assert_eq!(result, "bar");
        conn.del::<&str, ()>("foo").await.unwrap();

        // also create a stream
        conn.xgroup_create::<&str, &str, &str, ()>(DEFAULT_THREAD, "group-1", "0")
            .await
            .unwrap_or(());

        tracing::debug!("successfully connected to redis and pinged it");

        DataConnector {
            pool: PoolKind::Redis(pool.clone()),
        }
    } else {
        // default to internal pool
        DataConnector {
            pool: PoolKind::Internal(InternalPool::default()),
        }
    };

    // build our application with some routes
    let app = Router::new()
        .route("/", get(index_page))
        .route("/sse", get(sse_handler))
        .route("/get", get(get_messages))
        .route("/add", post(add_message_with_body))
        .route("/threads", get(get_threads))
        .route("/subscriptions", get(subscriptions_sse))
        .route("/flush", get(flush_messages))
        .with_state(my_struct)
        .into_make_service_with_connect_info::<SocketAddr>();

    let port = std::env::var("PORT").unwrap_or_else(|_| "3000".to_string());
    let host = std::env::var("HOST").unwrap_or_else(|_| "0.0.0.0".to_string());
    let listener = tokio::net::TcpListener::bind(format!("{}:{}", host, port))
        .await
        .unwrap();
    tracing::debug!("listening on {}", listener.local_addr().unwrap());
    axum::serve(listener, app).await.unwrap();
}

pub async fn index_page() -> Html<String> {
    Html(INDEX_HTML.to_string())
}

// handle get requests and filter by the supplied start and end times
async fn get_messages(
    params: Query<Params>,
    State(my_struct): State<ConnectionPool>,
) -> Result<Json<Vec<Message>>, (StatusCode, String)> {
    let key = params.thread.as_deref().unwrap_or(DEFAULT_THREAD);

    match my_struct.pool {
        PoolKind::Redis(pool) => {
            let mut conn = pool.get().await.map_err(internal_error)?;
            let start = params.start.as_deref().unwrap_or("-");
            let end = params.end.as_deref().unwrap_or("+");
            let results: redis::RedisResult<redis::streams::StreamRangeReply> =
                conn.xrange(key, start, end).await;
            match results {
                Ok(reply) => {
                    let typed_messages: Vec<Message> = reply
                        .ids
                        .into_iter()
                        .map(|value| Message {
                            message: value.get("message").unwrap_or_default(),
                            client_id: value.get("client_id").unwrap_or_default(),
                        })
                        .collect();
                    Ok(Json(typed_messages))
                }
                Err(err) => {
                    println!("Error: {:?}", err);
                    Err(internal_error(err))
                }
            }
        }
        PoolKind::Internal(internal_pool) => {
            let log = &internal_pool.logs.get_log(key).unwrap().clone();

            // u64 of time in microseconds
            let start = match params.start.as_deref() {
                Some(start) => start.parse::<u64>().unwrap_or(0),
                None => 0,
            };

            let end = match params.end.as_deref() {
                Some(end) => end.parse::<u64>().unwrap_or(u64::MAX),
                None => u64::MAX,
            };

            let messages = log.get_range(start, end);

            // convert LogEntry to Message
            let messages: Vec<Message> = messages
                .into_iter()
                .map(|entry| {
                    // parse to InternalEntry
                    let entry: InternalEntry =
                        serde_json::from_str(&entry.data).unwrap_or_default();
                    Message {
                        message: entry.message,
                        client_id: entry.client_id,
                    }
                })
                .collect();

            Ok(Json(messages))
        }
    }
}

async fn get_threads(
    State(my_struct): State<ConnectionPool>,
) -> Result<Json<Vec<String>>, (StatusCode, String)> {
    let keys: Vec<String> = match my_struct.pool {
        PoolKind::Redis(pool) => {
            let mut conn = pool.get().await.map_err(internal_error)?;
            let keys: Vec<String> = conn.keys("*").await.map_err(internal_error)?;
            // filter out the subscriptions key
            keys.into_iter()
                .filter(|key| !key.ends_with("_subscriptions"))
                .collect()
        }
        PoolKind::Internal(internal_pool) => internal_pool
            .logs
            .logs
            .lock()
            .unwrap()
            .keys()
            .filter(|key| !key.ends_with("_subscriptions"))
            .cloned()
            .collect(),
    };
    Ok(Json(keys))
}

// Handle long-lived connections and check and send new messages every second
async fn sse_handler(
    params: Query<Params>,
    State(my_struct): State<ConnectionPool>,
    ConnectInfo(addr): ConnectInfo<SocketAddr>,
) -> Result<Sse<impl Stream<Item = Result<Event, Infallible>>>, (StatusCode, String)> {
    let key = params
        .thread
        .clone()
        .unwrap_or_else(|| DEFAULT_THREAD.to_string());
    let start = params.start.clone().unwrap_or_else(|| "-".to_string());
    let async_stream = async_stream::stream! {
        match my_struct.pool {
            PoolKind::Redis(pool) => {
                let mut conn: PooledConnection<RedisConnectionManager> = pool.get().await.unwrap();

                // Ensure stream exists
                conn.xgroup_create_mkstream::<&str, &str, &str, ()>(&key, "group-1", "0")
                    .await
                    .unwrap_or(());

                let subscription_key = format!("{}_subscriptions", key);
                let client_id = params.identifier.clone().unwrap_or_else(|| addr.to_string());

                // Add client to the subscription set
                conn.sadd::<&str, &str, ()>(&subscription_key, &client_id).await.unwrap();

                // Clean up subscription on disconnect
                let _guard = scopeguard::guard((), |_| {
                    let pool = pool.clone();
                    let subscription_key = subscription_key.clone();
                    let client_id = client_id.clone();
                    tokio::spawn(async move {
                        let mut conn = pool.get().await.unwrap();
                        conn.srem::<&str, &str, ()>(&subscription_key, &client_id).await.unwrap();
                    });
                });

                let mut last_id = start;
                loop {
                    let results: redis::RedisResult<redis::streams::StreamRangeReply> =
                        conn.xrange(&key, last_id.as_str(), "+").await;
                    match results {
                        Ok(reply) => {
                            for value in reply.ids.into_iter() {
                                if value.id == last_id {
                                    continue;
                                }
                                last_id.clone_from(&value.id);
                                let raw_message: String = value.get("message").unwrap_or_default();
                                // parse into json object
                                let value2: Value = serde_json::from_str(&raw_message).unwrap_or_default();
                                let data = Message {
                                    message: value2.to_string(),
                                    client_id: value.get("client_id").unwrap_or_default(),
                                };
                                yield Event::default().data(serde_json::to_string(&data).unwrap_or_default());
                            }
                        }
                        Err(_err) => {
                            // TODO: handle error
                        }
                    }

                    tokio::time::sleep(Duration::from_secs(1)).await;
                }
            }
            PoolKind::Internal(internal_pool) => {
                let start = start.parse::<u64>().unwrap_or(0);
                let mut last_id = start;
                loop{
                    let log = internal_pool.logs.get_log(&key).unwrap_or_else(|| {
                        internal_pool.logs.create_log(&key);
                        internal_pool.logs.get_log(&key).unwrap()
                    });
                    let messages = log.get_range(last_id, u64::MAX);
                    for entry in messages {
                        let entry: InternalEntry = serde_json::from_str(&entry.data).unwrap_or_default();
                        let data = Message {
                            message: entry.message,
                            client_id: entry.client_id,
                        };
                        yield Event::default().data(serde_json::to_string(&data).unwrap_or_default());
                    }
                    last_id = Log::current_microseconds();
                    tokio::time::sleep(Duration::from_millis(200)).await;

                }
            }
        }
    };

    let stream = async_stream.map(Ok);
    Ok(Sse::new(stream).keep_alive(
        axum::response::sse::KeepAlive::new()
            .interval(Duration::from_secs(1))
            .text("keep-alive-text"),
    ))
}

/// Subscribe to the the list of subscribers for the specified thread (connected parties)
async fn subscriptions_sse(
    params: Query<Params>,
    State(my_struct): State<ConnectionPool>,
) -> Result<Sse<impl Stream<Item = Result<Event, Infallible>>>, (StatusCode, String)> {
    let key = params
        .thread
        .clone()
        .unwrap_or_else(|| DEFAULT_THREAD.to_string());
    let subscription_key = format!("{}_subscriptions", key);
    let async_stream = async_stream::stream! {
        match my_struct.pool {
            PoolKind::Redis(pool) => {
                let pool_clone = pool.clone();
                let mut conn: PooledConnection<RedisConnectionManager> = pool_clone.get().await.unwrap();
                tokio::time::sleep(Duration::from_millis(200)).await;
                loop {
                    let subscribers: Vec<String> = conn
                        .smembers(&subscription_key)
                        .await
                        .unwrap_or_default();
                    let data = serde_json::to_string(&subscribers).unwrap_or_default();
                    yield Event::default().data(data);
                    tokio::time::sleep(Duration::from_secs(5)).await;
                }
            }
            PoolKind::Internal(internal_pool) => {
                tokio::time::sleep(Duration::from_millis(200)).await;
                loop {
                    let subscribers: Vec<String> = internal_pool
                        .kv
                        .get(&subscription_key)
                        .unwrap_or(&"".to_string())
                        .split(',')
                        .map(|s| s.to_string())
                        .collect();
                    let data = serde_json::to_string(&subscribers).unwrap_or_default();
                    yield Event::default().data(data);
                    tokio::time::sleep(Duration::from_secs(5)).await;
                }
            }
        }
    };
    let stream = async_stream.map(Ok);
    Ok(Sse::new(stream).keep_alive(
        axum::response::sse::KeepAlive::new()
            .interval(Duration::from_secs(1))
            .text("keep-alive-text"),
    ))
}

// Add a message to the specified thread
async fn add_message_with_body(
    params: Query<Params>,
    State(my_struct): State<ConnectionPool>,
    ConnectInfo(addr): ConnectInfo<SocketAddr>,
    Json(body): Json<MyEnum>,
) -> Result<Response, (StatusCode, String)> {
    let mut client_id = params
        .identifier
        .clone()
        .unwrap_or_else(|| addr.to_string());

    // replace any : with _
    client_id = client_id.replace(':', "_");

    let key = params
        .thread
        .clone()
        .unwrap_or_else(|| DEFAULT_THREAD.to_string());

    match my_struct.pool {
        PoolKind::Redis(pool) => {
            let body = match body {
                MyEnum::String(s) => MyEnum::Value(serde_json::json!({
                    "simple_message": {
                        "room": "default",
                        "message": s,
                        "score": 0
                    }
                })),
                _ => body,
            };

            let mut conn = pool.get().await.map_err(internal_error)?;
            let json_response = serde_json::to_string(&body).map_err(internal_error)?;

            // Ensure stream exists
            conn.xgroup_create_mkstream::<&str, &str, &str, ()>(&key, "group-1", "0")
                .await
                .unwrap_or(());

            conn.xadd(
                &key,
                "*",
                &[
                    ("message", json_response.as_str()),
                    ("client_id", client_id.as_str()),
                ],
            )
            .await
            .map_err(internal_error)?;

            Ok((StatusCode::OK, Json(body)).into_response())
        }
        PoolKind::Internal(internal_pool) => {
            let message: String = match &body {
                MyEnum::String(s) => s.clone(),
                MyEnum::Value(v) => v.to_string(),
            };
            let entry = InternalEntry {
                message: message.clone(),
                client_id: client_id.clone(),
            };

            let thread = internal_pool.logs.get_log(&key).unwrap_or_else(|| {
                internal_pool.logs.create_log(&key);
                internal_pool.logs.get_log(&key).unwrap()
            });

            thread.append(serde_json::to_string(&entry).unwrap_or_default());
            Ok((StatusCode::OK, Json(body)).into_response())
        }
    }
}

/// Flush all messages from the specified thread
async fn flush_messages(
    params: Query<Params>,
    State(my_struct): State<ConnectionPool>,
) -> Result<Response, (StatusCode, String)> {
    let key = params
        .thread
        .clone()
        .unwrap_or_else(|| DEFAULT_THREAD.to_string());
    match my_struct.pool {
        PoolKind::Redis(pool) => {
            let mut conn = pool.get().await.map_err(internal_error)?;
            conn.del(&key).await.map_err(internal_error)?;
        }
        PoolKind::Internal(internal_pool) => {
            internal_pool.logs.get_log(&key).unwrap().flush();
        }
    }
    Ok((StatusCode::OK, "Messages flushed".to_string()).into_response())
}

/// Utility function for mapping any error into a `500 Internal Server Error`
/// response.
fn internal_error<E>(err: E) -> (StatusCode, String)
where
    E: std::error::Error,
{
    println!("Error: {:?}", err);
    (StatusCode::INTERNAL_SERVER_ERROR, err.to_string())
}
