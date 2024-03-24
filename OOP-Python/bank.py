import uuid

class Account:
    def __init__(self, name):
        """Initialize the account with name, balance, and a unique account number."""
        self.name = name
        self.balance = 0
        self.account_number = uuid.uuid4()

    def __str__(self):
        """Return a string representation of the account."""
        return f"{self.name} - {self.account_number}"

    def account_info(self):
        """Print the account holder's name and current balance."""
        print(f"{self.name} Updated balance: {self.balance}")

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.balance += amount
        self.account_info()

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.account_info()
        return True


# Create a new account
account1 = Account("John Doe")

# Display the account details
print("Account Details:")
print(account1)

# Deposit money into the account
account1.deposit(1000)

# Withdraw money from the account
try:
    account1.withdraw(500)
except ValueError as e:
    print(e)  # Handle insufficient funds error

# Attempt to withdraw more than the balance
try:
    account1.withdraw(700)
except ValueError as e:
    print(e)  # Handle insufficient funds error

# Display the final account details
print("Final Account Details:")
print(account1)
