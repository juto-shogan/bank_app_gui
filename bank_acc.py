from tkinter import *
from subprocess import call

root = Tk()
class BankAccount:
    # functions
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")


def open_accounts_window():
    name = name_entry.get()
    account_number = account_number_entry.get()



    if len(account_number) != 10:
        print("Incorrect account number. Please enter a 10-digit account number.")
        return

    accounts_window = Toplevel(root)
    accounts_window.title("Bank Accounts")

    name_label = Label(accounts_window, text=f"Welcome, {name}! Account Number: {account_number}")
    name_label.grid(row=0, column=0, columnspan=4)

    current_account = BankAccount("Current")
    savings_account = BankAccount("Savings")

    savings_balance = Label(accounts_window, text="Savings Account Balance: 0")
    savings_balance.grid(row=4, column=0)



root.title("Bank App")

name_label = Label(root, text="Enter Your Name:")
name_label.grid(row=0, column=0)

name_entry = Entry(root)
name_entry.grid(row=0, column=1)

account_number_label = Label(root, text="Enter Your Account Number:")
account_number_label.grid(row=1, column=0)

account_number_entry = Entry(root)
account_number_entry.grid(row=1, column=1)

open_accounts_button = Button(root, text="Open Accounts", command=open_accounts_window)
open_accounts_button.grid(row=2, column=0)

root.mainloop()