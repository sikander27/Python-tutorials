import uuid

class Account:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 0
        self.account_number = uuid.uuid4()

    def __str__(self) -> str:
        return f"{self.name} - {self.account_number}"

    def account_info(self):
        print(f"{self.name} Updated balance {self.balance}")

    def deposit(self, ammount):
        self.balance += ammount
        return self.account_info()

    def withdraw(self, ammount):
        if ammount > self.balance:
            print("Invalid Balance")
            return 0
        self.balance -= ammount
        self.account_info()
        return ammount



a1 = Account('sikander')
print(a1)
a1.deposit(10000)
a1.withdraw(5000)
a1.withdraw(10000)