import uuid
from typing import List
from user import User
from split import Split

class Expense:
    def __init__(self, description, amount, paid_by, splits):
        self.id = uuid.uuid4()
        self.description = description
        self.amount = amount
        self.paid_by: User = paid_by
        self.splits: List[Split] = splits