from Transactions import Transaction
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