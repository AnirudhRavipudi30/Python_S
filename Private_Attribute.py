class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (with __)

    def get_balance(self):  # Getter
        return self.__balance

    def set_balance(self, amount):  # Setter
        if amount >= 0:
            self.__balance = amount

# Creating an Object
account = BankAccount("Alice", 1000)

# Accessing Private Attribute (Wrong)
# print(account.__balance)  # ❌ AttributeError

# Accessing via Getter
print(account.get_balance())  # ✅ Output: 1000

# Modifying via Setter
account.set_balance(2000)
print(account.get_balance())  # ✅ Output: 2000