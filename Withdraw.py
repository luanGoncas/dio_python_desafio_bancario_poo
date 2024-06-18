import Transaction

class Withdraw(Transaction):
    def __init__(self, value):
        super().__init()
        self.__value = value