from abc import ABC, abstractmethod
from message import Message

class Subscriber(ABC):
    @abstractmethod
    def on_message(self, message: Message):
        pass

class EmailSubscriber(Subscriber):
    def on_message(self, message):
        print(f"[EmailSubscriber] Received: {message.payload}")

class LoggingSubscriber(Subscriber):
    def on_message(self, message):
        print(f"[LoggingSubscriber] Received: {message.payload}")