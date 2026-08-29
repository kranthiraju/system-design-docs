from user import User
from group import Group
from expense import Expense
from split import EqualSplit, ExactSplit, PercentageSplit
from splitwise_service import SplitwiseService


class SplitwiseDemo:

    @staticmethod
    def main():
        splitwise = SplitwiseService()

        # Create users
        alice = User("Alice")
        bob = User("Bob")
        charlie = User("Charlie")

        splitwise.add_user(alice)
        splitwise.add_user(bob)
        splitwise.add_user(charlie)

        # Create group
        group = Group("Goa Trip")

        group.add_member(alice)
        group.add_member(bob)
        group.add_member(charlie)

        splitwise.create_group(group)

        # ------------------------------------------------
        # Test Case 1: Equal Split
        # ------------------------------------------------
        print("\n===== TEST 1: Equal Split =====")

        expense1 = Expense(
            description="Dinner",
            paid_by=alice,
            amount=900,
            splits=[
                EqualSplit(alice),
                EqualSplit(bob),
                EqualSplit(charlie)
            ]
        )

        splitwise.add_expense(expense1, group)

        splitwise.show_balance(alice)
        splitwise.show_balance(bob)
        splitwise.show_balance(charlie)

        # ------------------------------------------------
        # Test Case 2: Exact Split
        # ------------------------------------------------
        print("\n===== TEST 2: Exact Split =====")

        expense2 = Expense(
            description="Lunch",
            paid_by=bob,
            amount=1000,
            splits=[
                ExactSplit(alice, 200),
                ExactSplit(bob, 300),
                ExactSplit(charlie, 500)
            ]
        )

        splitwise.add_expense(expense2, group)

        splitwise.show_balance(alice)
        splitwise.show_balance(bob)
        splitwise.show_balance(charlie)

        # ------------------------------------------------
        # Test Case 3: Percentage Split
        # ------------------------------------------------
        print("\n===== TEST 3: Percentage Split =====")

        expense3 = Expense(
            description="Breakfast",
            paid_by=charlie,
            amount=2000,
            splits=[
                PercentageSplit(alice, 50),
                PercentageSplit(bob, 30),
                PercentageSplit(charlie, 20)
            ]
        )

        splitwise.add_expense(expense3, group)

        splitwise.show_balance(alice)
        splitwise.show_balance(bob)
        splitwise.show_balance(charlie)


if __name__ == "__main__":
    SplitwiseDemo.main()
