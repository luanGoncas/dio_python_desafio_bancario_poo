from Transactions.Transaction import Transaction
from Accounts.Account import Account

class Deposit(Transaction):
    def __init__(self, value: float):
        super().__init()
        self.__value = value
    
    @property
    def value(self):
        return self.__value or 0
    
    def register(self, account: Account):
        if account.deposit(self.__value):
            account.statement.add_transaction(self)