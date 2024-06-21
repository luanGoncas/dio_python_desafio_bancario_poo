from Transactions import Transaction

class Withdraw(Transaction):
    def __init__(self, value):
        super().__init()
        self.__value = value
    
    @property
    def value(self):
        return f'WITHDRAW: R$ {self.__value}' or 0