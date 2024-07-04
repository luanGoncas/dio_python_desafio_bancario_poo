from Transactions.Transaction import Transaction

class Withdraw(Transaction):
    def __init__(self, value: float):
        self.__value = value
    
    @property
    def value(self):
        return self.__value or 0.0
    
    def register(self, account):
        if account.withdraw(self.__value):
            account.statement.add_transaction(self)