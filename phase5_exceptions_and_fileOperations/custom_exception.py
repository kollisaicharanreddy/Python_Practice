class NegativeBalanceError(Exception):
    pass

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("The amount exceeds the balance")
        self.balance -= amount
        return amount
try:
    wallet = Wallet(10000)
    wallet.withdraw(15000)
except NegativeBalanceError:
    print("Insufficient balance")
else:
    print("Withdrawal successful")
finally:
    print("Execution Completed")