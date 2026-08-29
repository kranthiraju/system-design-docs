import uuid
from notification_type import NotificationType

class Notification:
    def __init__(self, title, message, type):
        self.id: str = uuid.uuid4()
        self.title: str = title
        self.message: str = message
        self.type: NotificationType = type