# account
class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"deposit was successful.balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def print_details(self):
        print(f"Account number: {self.acc_number}")
        print(f"Account name: {self.name}")
        print(f"Account balance: {self.balance}")
        print("---------------------------------")


acc1 = Account("987", "Jackson", 10000)
acc1.deposit(1300)
acc1.withdraw(300)
acc1.print_details()



acc2 = Account("546", "Maryanne", 90000)
acc2.deposit(1200)
acc2.withdraw(400)
acc2.print_details()



acc3 = Account("786", "Johnson", 70000)
acc3.deposit(1500)
acc3.withdraw(2500)
acc3.print_details()
