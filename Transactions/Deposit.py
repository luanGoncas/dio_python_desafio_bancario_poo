import Transaction
from Accounts import Account

class Deposit(Transaction):
    def __init__(self, value: float):
        super().__init()
        self.__value = value
    
    @property
    def value(self):
        return f'DEPOSIT: R$ {self.__value}' or 0
    
    def register(self, account: Account):
        account.__statement += self.value
        account.__statement += '\n'