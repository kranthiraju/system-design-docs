from abc import ABC, abstractmethod
from log_message import LogMessage
from log_formatter import LogFormatter

class LogAppender(ABC):
    def __init__(self, formatter: LogFormatter):
        self.formatter = formatter

    @abstractmethod
    def append(self, log_message:LogMessage):
        pass

class ConsoleAppender(LogAppender):
    def append(self, log_message: LogMessage):
        formatted_message = self.formatter.format(log_message)
        print(f"[CONSOLE] {formatted_message}")


class FileAppender(LogAppender):
    def __init__(self, formatter, file_name):
        self.formatter = formatter
        self.file_name = file_name

    def append(self, log_message: LogMessage):
        formatted_message = self.formatter.format(log_message)
        print(f"[FILE-{self.file_name}] {formatted_message}")