from broker import Broker
from subscriber import EmailSubscriber, LoggingSubscriber
from message import Message


class PubSubDemo:

    @staticmethod
    def main():
        print("========== Pub-Sub Demo Started ==========\n")

        broker = Broker()

        # Create subscribers
        print("Creating subscribers...")
        sub1 = EmailSubscriber()
        sub2 = LoggingSubscriber()

        print("  - EmailSubscriber")
        print("  - LoggingSubscriber\n")

        # Create messages
        print("Creating messages...")
        msg1 = Message("This is sports message.")
        msg2 = Message("This is sports message 34.")
        msg3 = Message("This is films message.")

        # Subscribe
        print("\n========== SUBSCRIBE ==========")

        print("EmailSubscriber subscribing to sports")
        broker.subscribe("sports", sub1)

        print("EmailSubscriber subscribing to films")
        broker.subscribe("films", sub1)

        print("LoggingSubscriber subscribing to films")
        broker.subscribe("films", sub2)

        # Publish
        print("\n========== PUBLISH ==========")

        print("\nPublishing to sports...")
        broker.publish("sports", msg1)

        print("\nPublishing to films...")
        broker.publish("films", msg3)

        # Unsubscribe
        print("\n========== UNSUBSCRIBE ==========")

        print("EmailSubscriber unsubscribing from films")
        broker.unsubscribe("films", sub1)

        # Publish again after unsubscribe
        print("\n========== PUBLISH AFTER UNSUBSCRIBE ==========")

        print("\nPublishing to films again...")
        broker.publish("films", msg2)

        print("\nPublishing to sports again...")
        broker.publish("sports", msg2)

        print("\n========== Pub-Sub Demo Finished ==========")


PubSubDemo.main()
