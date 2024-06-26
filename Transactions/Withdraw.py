from Transactions import Transaction
from Accounts import Account

class Withdraw(Transaction):
    def __init__(self, value: float):
        super().__init()
        self.__value = value
    
    @property
    def value(self):
        return self.__value or 0
    
    def register(self, account: Account):
        if account.withdraw(self.__value):
            account.statement.add_transaction(self)