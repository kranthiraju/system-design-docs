import uuid
from typing import Set, List
from user import User
from expense import Expense

class Group:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.members: Set[User] = set()
        self.expenses: List[Expense] = []

    def add_member(self, member: User):
        self.members.add(member)

    def add_expenses(self, expense: Expense):
        self.expenses.append(expense)
