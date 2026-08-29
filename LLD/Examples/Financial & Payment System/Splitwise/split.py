from abc import ABC, abstractmethod
from user import User


class Split(ABC):
    def __init__(self, user: User):
        self.user = user
        self.amount = 0

    @abstractmethod
    def calculate_amount(self, total_amount, total_users):
        pass


class EqualSplit(Split):
    def calculate_amount(self, total_amount, total_users):
        self.amount = total_amount / total_users
        return self.amount


class ExactSplit(Split):
    def __init__(self, user: User, amount):
        super().__init__(user)
        self.amount = amount

    def calculate_amount(self, total_amount, total_users):
        return self.amount


class PercentageSplit(Split):
    def __init__(self, user: User, percentage):
        super().__init__(user)
        self.percentage = percentage

    def calculate_amount(self, total_amount, total_users):
        self.amount = total_amount * self.percentage / 100
        return self.amount
