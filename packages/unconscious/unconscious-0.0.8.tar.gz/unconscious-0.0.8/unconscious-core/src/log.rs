use std::clone::Clone;
use std::collections::HashMap;
use std::collections::{BTreeMap, VecDeque};
use std::sync::{Arc, Mutex};
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Clone, Debug)]
pub struct LogEntry {
    pub offset: u64,
    pub data: String,
}

#[derive(Clone, Debug)]
pub struct Log {
    entries: Arc<Mutex<VecDeque<LogEntry>>>,
    index: Arc<Mutex<BTreeMap<u64, usize>>>,
}

impl Log {
    pub fn new() -> Self {
        Log {
            entries: Arc::new(Mutex::new(VecDeque::new())),
            index: Arc::new(Mutex::new(BTreeMap::new())),
        }
    }

    pub fn append(&self, data: String) {
        let mut entries = self.entries.lock().unwrap();
        let mut index = self.index.lock().unwrap();

        let offset = Self::current_microseconds();
        let entry = LogEntry { offset, data };
        let len = entries.len();
        entries.push_back(entry);
        index.insert(offset, len);
    }

    pub fn get(&self, offset: u64) -> Option<LogEntry> {
        let entries = self.entries.lock().unwrap();
        let index = self.index.lock().unwrap();

        index
            .get(&offset)
            .and_then(|&pos| entries.get(pos).cloned())
    }

    pub fn get_range(&self, start: u64, end: u64) -> Vec<LogEntry> {
        let entries = self.entries.lock().unwrap();
        let index = self.index.lock().unwrap();

        index
            .range(start..end)
            .filter_map(|(_, &pos)| entries.get(pos).cloned())
            .collect()
    }

    pub fn current_microseconds() -> u64 {
        let duration = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        duration.as_secs() * 1_000_000 + u64::from(duration.subsec_micros())
    }

    pub fn flush(&self) {
        let mut entries = self.entries.lock().unwrap();
        let mut index = self.index.lock().unwrap();

        entries.clear();
        index.clear();
    }
}

#[derive(Clone)]
pub struct LogManager {
    pub logs: Arc<Mutex<HashMap<String, Log>>>,
}

impl LogManager {
    pub fn new() -> Self {
        LogManager {
            logs: Arc::new(Mutex::new(HashMap::new())),
        }
    }

    pub fn create_log(&self, name: &str) {
        let mut logs = self.logs.lock().unwrap();
        logs.insert(name.to_string(), Log::new());
    }

    pub fn get_log(&self, name: &str) -> Option<Log> {
        let logs = self.logs.lock().unwrap();
        logs.get(name).cloned()
    }

    #[allow(dead_code)]
    pub fn append_to_log(&self, name: &str, data: String) {
        if let Some(log) = self.get_log(name) {
            log.append(data);
        }
    }

    #[allow(dead_code)]
    pub fn get_from_log(&self, name: &str, offset: u64) -> Option<LogEntry> {
        if let Some(log) = self.get_log(name) {
            log.get(offset)
        } else {
            None
        }
    }

    #[allow(dead_code)]
    pub fn get_range_from_log(&self, name: &str, start: u64, end: u64) -> Vec<LogEntry> {
        if let Some(log) = self.get_log(name) {
            log.get_range(start, end)
        } else {
            Vec::new()
        }
    }
}
