from Accounts.Account import Account
from Accounts.CurrentAccount import CurrentAccount
from Transactions.Deposit import Deposit
from Transactions.Statement import Statement
from Transactions.Transaction import Transaction
from Transactions.Withdraw import Withdraw
from Users.Client import Client
from Users.PhysicalPerson import PhysicalPerson

print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))