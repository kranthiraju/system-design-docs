from typing import Dict
from user import User
from group import Group
from expense import Expense
from balance_sheet import BalanceSheet


class SplitwiseService:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, Group] = {}
        self.balance_sheet = BalanceSheet()

    def add_user(self, user: User):
        if user.id in self.users:
            print("User already exists!!!")
            return

        self.users[user.id] = user

    def create_group(self, group: Group):
        if group.id in self.groups:
            print("Group already exists!!!")
            return

        self.groups[group.id] = group

    def add_expense(self, expense: Expense, group: Group):
        if group.id not in self.groups:
            print("Group not found!!!")
            return

        # Check payer
        if expense.paid_by not in group.members:
            print("Payer is not a member of the group")
            return

        # Check all users
        for split in expense.splits:
            if split.user not in group.members:
                print(f"{split.user.name} is not a group member")
                return

        # Calculate split amounts
        total_users = len(expense.splits)

        total_split_amount = 0

        for split in expense.splits:
            amount = split.calculate_amount(
                expense.amount,
                total_users
            )

            total_split_amount += amount

        # Validate total
        if round(total_split_amount, 2) != round(expense.amount, 2):
            print("Split amounts do not match expense amount")
            return

        # Store expense in group
        group.add_expenses(expense)

        # Update balance sheet
        for split in expense.splits:
            if split.user == expense.paid_by:
                continue

            self.balance_sheet.add_debt(
                split.user,
                expense.paid_by,
                split.amount
            )

    def show_balance(self, user: User):
        if user.id not in self.users:
            print("User does not exist")
            return

        balances = self.balance_sheet.get_balances(user)

        if not balances:
            print("No balances")
            return

        for balance in balances:
            print(balance)

    def settle(self, from_user: User, to_user: User, amount):
        self.balance_sheet.settle(
            from_user,
            to_user,
            amount
        )
