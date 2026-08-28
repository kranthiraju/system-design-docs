from typing import Dict
from collections import defaultdict
from subscriber import Subscriber
from message import Message
from topic import Topic

class Broker:
    def __init__(self):
        self.topics: Dict[str, Topic] = defaultdict()

    def subscribe(self, topic_name: str, subscriber: Subscriber):
        """
        add that subscriber to topic if exist or create new topic then add
        """ 
        if topic_name not in self.topics.keys():
            # create new topic and add subscriber
            new_topic = Topic(topic_name)
            new_topic.subscribe(subscriber)
            self.topics[topic_name] = new_topic
        else:
            self.topics[topic_name].subscribe(subscriber)

    def unsubscribe(self, topic_name: str, subscriber: Subscriber):
        """
        remove that subscriber from requested topic
        if not return error
        """
        if topic_name not in self.topics.keys():
            print(f"{topic_name} - Topic not present!!")
            return

        self.topics[topic_name].unsubscribe(subscriber)
        

    def publish(self, topic_name: str, message: Message):
        """
        publish that message to topic
        """
        if topic_name not in self.topics.keys():
            print(f"{topic_name} - Topic not present!!")
            return

        subscribers = self.topics[topic_name].subscribers
        for subscribe in subscribers:
            subscribe.on_message(message)