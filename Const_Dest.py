class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"🏦 Account for {self.name} created with balance ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 Deposited ${amount}. New balance: ${self.balance}")

    def __del__(self):
        print(f"❌ Account for {self.name} is being closed!")

# Creating an Object (Constructor runs automatically)
account1 = BankAccount("Alice", 500)

# Depositing Money
account1.deposit(200)

# Deleting Object (Destructor runs automatically)
del account1