from datetime import datetime
from abc import ABC, abstractmethod
from log_message import LogMessage


class LogFormatter(ABC):
    @abstractmethod
    def format(self, log_message) -> str:
        pass


class TextFormatter(LogFormatter):
    def format(self, log_message: LogMessage) -> str:
        return f"{datetime.fromtimestamp(log_message.timestamp)} [{log_message.level.value}] : {log_message.message}"


class JSONFormatter(LogFormatter):
    def format(self, log_message: LogMessage) -> str:
        return (
            f"{{"
            f'"timestamp": "{datetime.fromtimestamp(log_message.timestamp).isoformat()}", '
            f'"level": "{log_message.level.value}", '
            f'"message": "{log_message.message}"'
            f"}}"
        )
