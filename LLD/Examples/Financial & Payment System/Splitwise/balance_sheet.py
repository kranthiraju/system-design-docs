class BalanceSheet:
    def __init__(self):
        # balances[from_user][to_user] = amount
        self.balances = {}

    def get_balance(self, from_user, to_user):
        return self.balances.get(from_user, {}).get(to_user, 0)

    def add_debt(self, from_user, to_user, amount):
        if amount <= 0:
            return

        if from_user == to_user:
            return

        if from_user not in self.balances:
            self.balances[from_user] = {}

        # Check if to_user already owes from_user
        reverse_amount = self.get_balance(to_user, from_user)

        if reverse_amount > 0:
            if reverse_amount >= amount:
                self.balances[to_user][from_user] -= amount

                if self.balances[to_user][from_user] == 0:
                    del self.balances[to_user][from_user]

                return
            else:
                self.balances[to_user][from_user] = 0
                del self.balances[to_user][from_user]

                amount -= reverse_amount

        self.balances[from_user][to_user] = (
            self.get_balance(from_user, to_user) + amount
        )

    def settle(self, from_user, to_user, amount):
        current_debt = self.get_balance(from_user, to_user)

        if current_debt <= 0:
            print("No debt exists between these users")
            return

        if amount <= 0:
            print("Amount must be positive")
            return

        if amount > current_debt:
            print("Settlement exceeds outstanding debt")
            return

        self.balances[from_user][to_user] -= amount

        if self.balances[from_user][to_user] == 0:
            del self.balances[from_user][to_user]

        if not self.balances[from_user]:
            del self.balances[from_user]

    def get_balances(self, user):
        result = []

        # What this user owes
        for to_user, amount in self.balances.get(user, {}).items():
            if amount > 0:
                result.append(
                    f"{user.name} owes {to_user.name}: {amount}"
                )

        # What others owe this user
        for from_user, debts in self.balances.items():
            amount = debts.get(user, 0)

            if amount > 0:
                result.append(
                    f"{from_user.name} owes {user.name}: {amount}"
                )

        return result
