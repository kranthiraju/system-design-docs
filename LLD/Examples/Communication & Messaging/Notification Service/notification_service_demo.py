from notification_service import NotificationService
from user import User
from notification_channel import EmailChannel, SMSChannel, PushChannel
from user_preference_service import UserPreferenceService
from user_preference import UserPreference
from notification import Notification
from notification_type import NotificationType


class NotificationServiceDemo:
    @staticmethod
    def main():

        print("=" * 60)
        print("        NOTIFICATION SYSTEM DEMO")
        print("=" * 60)

        # Services
        user_preference_service = UserPreferenceService()
        notification_service = NotificationService(user_preference_service)

        # Channels
        email_channel = EmailChannel()
        sms_channel = SMSChannel()
        push_channel = PushChannel()

        notification_service.set_channels("email", email_channel)
        notification_service.set_channels("sms", sms_channel)
        notification_service.set_channels("push", push_channel)

        print("\nNotification channels registered:")
        print("- Email")
        print("- SMS")
        print("- Push")

        # Users
        user1 = User(
            "UA_02",
            "Apple",
            "apple@app.com",
            "9402",
            "tk_090"
        )

        user2 = User(
            "UA_32",
            "Google",
            "google@app.com",
            "8483",
            "tk_017"
        )

        print("\nUsers created:")
        print(f"- {user1.name}")
        print(f"- {user2.name}")

        # Preferences
        user_preference1 = UserPreference(
            True,   # Email
            True,   # SMS
            True    # Push
        )

        user_preference2 = UserPreference(
            True,   # Email
            False,  # SMS
            True    # Push
        )

        user_preference_service.set_preference(
            user1.user_id,
            user_preference1
        )

        user_preference_service.set_preference(
            user2.user_id,
            user_preference2
        )

        # --------------------------------------------------
        # Test Case 1
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("TEST CASE 1: ORDER PLACED")
        print("=" * 60)

        notify1 = Notification(
            title="Order Placed",
            message="Your order has been successfully placed.",
            type=NotificationType.ORDER_PLACED
        )

        print(f"User: {user1.name}")
        print(f"Type: {notify1.type.value}")
        print(f"Message: {notify1.message}")

        notification_service.send(user1, notify1)

        # --------------------------------------------------
        # Test Case 2
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("TEST CASE 2: ORDER SHIPPED")
        print("=" * 60)

        notify2 = Notification(
            title="Order Shipped",
            message="Your order has been shipped.",
            type=NotificationType.ORDER_SHIPPED
        )

        print(f"User: {user2.name}")
        print(f"Type: {notify2.type.value}")
        print(f"Message: {notify2.message}")

        notification_service.send(user2, notify2)

        # --------------------------------------------------
        # Test Case 3
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("TEST CASE 3: ORDER DELIVERED")
        print("=" * 60)

        notify3 = Notification(
            title="Order Delivered",
            message="Your order has been delivered successfully.",
            type=NotificationType.ORDER_DELIVERED
        )

        print(f"User: {user1.name}")
        print(f"Type: {notify3.type.value}")
        print(f"Message: {notify3.message}")

        notification_service.send(user1, notify3)

        print("\n" + "=" * 60)
        print("             DEMO COMPLETED")
        print("=" * 60)


NotificationServiceDemo.main()
