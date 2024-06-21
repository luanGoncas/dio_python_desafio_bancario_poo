import Transaction

class Deposit(Transaction):
    def __init__(self, value):
        super().__init()
        self.__value = value
    
    @property
    def value(self):
        return f'DEPOSIT: R$ {self.__value}' or 0