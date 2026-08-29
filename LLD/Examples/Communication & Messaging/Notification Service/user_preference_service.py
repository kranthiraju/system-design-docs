from typing import Dict
from user_preference import UserPreference

class UserPreferenceService:
    def __init__(self):
        self.users_preference: Dict[str, UserPreference] = {}

    def set_preference(self, user_id: str, preference: UserPreference):
        self.users_preference[user_id] = preference

    def get_preference(self, user_id: str) -> UserPreference:
        return self.users_preference.get(user_id)