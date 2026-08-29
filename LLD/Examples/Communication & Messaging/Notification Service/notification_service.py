from typing import Dict
from notification_channel import NotificationChannel
from user_preference_service import UserPreferenceService
from notification import Notification
from user import User

class NotificationService:
    def __init__(self, preference_service):
        self.channels: Dict[NotificationChannel] = {}
        self.preference_service : UserPreferenceService = preference_service

    def set_channels(self, name:str, channel: NotificationChannel):
        self.channels[name] = channel

    def send(self, user: User, notification: Notification):
        """
        send the notification to user by preferred channels
        """
        preferred_channels = self.preference_service.get_preference(user_id= user.user_id)
        if not preferred_channels:
            print(f"User {user.name} has no preferences!!!")
            return

        if preferred_channels.email_enabled:
            self.channels["email"].send(user, notification)
        if preferred_channels.sms_enabled:
            self.channels["sms"].send(user, notification)
        if preferred_channels.push_enabled:
            self.channels["push"].send(user, notification)