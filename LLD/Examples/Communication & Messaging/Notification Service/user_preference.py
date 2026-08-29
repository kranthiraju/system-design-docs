class UserPreference:
    def __init__(self, email_enabled, sms_enabled, push_enabled):
        self.email_enabled : bool = email_enabled
        self.sms_enabled: bool = sms_enabled
        self.push_enabled: bool = push_enabled