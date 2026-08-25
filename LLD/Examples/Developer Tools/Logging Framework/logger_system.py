from typing import List
from log_message import LogMessage
from log_level import LogLevel
from log_formatter import LogFormatter, TextFormatter
from log_appender import LogAppender

class LoggerSystem:
    _instance = None
    def __init__(self):
      self.log_formatter = TextFormatter()
      self.log_appenders: List[LogAppender] = []

    def get_instance(self):
        if LoggerSystem._instance is None:
            LoggerSystem._instance = LoggerSystem()

        return LoggerSystem._instance

    def add_log_appenders(self, appender: LogAppender):
        self.log_appenders.append(appender)

    def set_log_formatter(self, formatter: LogFormatter):
        self.log_formatter = formatter

    def log(self, log_level, message):
        log_message = LogMessage(log_level, message)
        for appender in self.log_appenders:
             appender.append(log_message)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def warn(self, message):
        self.log(LogLevel.WARN, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)