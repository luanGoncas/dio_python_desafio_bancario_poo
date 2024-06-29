from Transactions.Transaction import Transaction
import datetime

class Statement:
    def __init__(self) -> None:
        self.__transactions = []
    
    @property
    def transactions(self):
        return self.__transactions or []

    @transactions.setter
    def add_transaction(self, transaction: Transaction):
        __transaction = transaction or None

        self.__transactions.append(
            {
                'Type': __transaction.__class__.name__,
                'Value': __transaction.value,
                'Data': datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}'