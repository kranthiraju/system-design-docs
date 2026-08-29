from abc import ABC, abstractmethod
from notification import Notification
from user import User

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, user:User, notification: Notification):
        pass

class EmailChannel(NotificationChannel):
    def send(self, user:User, notification: Notification):
        print(
            f"[EMAIL] To: {user.email}, "
            f"Message: {notification.message}"
        )

class SMSChannel(NotificationChannel):
    def send(self, user: User, notification: Notification):
        print(
            f"[SMS] To: {user.phone}, "
            f"Message: {notification.message}"
        )

class PushChannel(NotificationChannel):
    def send(self, user: User, notification: Notification):
        print(
            f"[PUSH] To: {user.device_token}, "
            f"Message: {notification.message}"
        )