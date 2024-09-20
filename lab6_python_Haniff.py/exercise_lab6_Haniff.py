"""Alisa Haniff
Excerise 6 Lab 6
python class"""

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Withdrawal of {amount} cannot be made.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")



# instance of the BankAccount class
useraccount = BankAccount("123456789", "Alisa")

#deposits and withdrawals
useraccount.withdraw(700)  
useraccount.deposit(1000)  
useraccount.withdraw(500)  

#final balance
print(f"Final balance: {useraccount.balance}")