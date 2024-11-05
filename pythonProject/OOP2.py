"""
Simple bank account system where we can deposit and check on balance
"""
# function with a default parameter
def create_account(balance=0):
    return {"balance": balance}
def deposit(current_account,amount):
    # we want to create a new copy of the existing dict.
    # {**account,....} unpacks the current key and value pairs in current account to create a new dictionary
    return {**current_account,"balance": current_account["balance"] + amount}
def withdraw(current_account,amount):
    if amount > current_account["balance"]:
        print("Insufficient funds")
        return current_account
    print(f"{amount} has been withdrawn")
    return {**current_account, "balance" : current_account["balance"] - amount}
def get_balance(current_account):
    return current_account["balance"]
# usage
account1 = create_account()
account1 = deposit(account1,100)
print("Balance" , get_balance(account1))
account1 = withdraw(account1,50)
print("Balance" , get_balance(account1))
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
# usage
account2 = BankAccount()
account2.deposit(100)
print(account2.get_balance())
account2.deposit(1000)
print(account2.get_balance())
account2.withdraw(500)
print(account2.get_balance())