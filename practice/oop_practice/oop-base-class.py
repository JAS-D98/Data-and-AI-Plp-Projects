class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Do you want to Deposit: {self.balance}")

    def withdraw(self, amount):
        if amount>self.balance:
            print("You have insufficient funds")
        else:
            self.balance=self.balance-amount
            print(f"You have successfully withdrawn {amount}, current balance is {self.balance}")

    def check_balance(self):
        print(f"{self.name} Here's your balance: {self.balance}")


user1=BankAccount("James", 1200)
user1.withdraw(1300)
user1.check_balance()