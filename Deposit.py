import Transaction

class Deposit(Transaction):
    def __init__(self, value):
        super().__init()
        self.__value = value