from typing import Set
from subscriber import Subscriber
from message import Message

class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers: Set[Subscriber] = set()

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, message: Message):
        for subscriber in self.subscribers:
            subscriber.on_message(message)