class ATM:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def display_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: +₹{amount:.2f}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew:  -₹{amount:.2f}")
            return True
        return False

    def get_statement(self):
        return self.transactions