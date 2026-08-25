import time
from log_level import LogLevel

class LogMessage:
    def __init__(self, level, message):
        self.level: LogLevel = level
        self.message = message
        self.timestamp = time.time()