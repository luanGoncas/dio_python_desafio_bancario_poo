from Accounts import Account
from Users import Client
from Transactions import Statement, Withdraw

class CurrentAccount(Account):
    def __init__(self, balance: float, number: int, client: Client, agency: str,
                 statement: Statement, limit: float, withdraw_limit: int):
        super().__init__(balance, number, client, agency, statement)
        self.__limit = limit
        self.__withdraw_limit = withdraw_limit
    
    def withdraw(self, value: float) -> bool:
        __value = value or 0
        __limit = self.__limit or 0
        __withdraw_limit = self.__withdraw_limit or 0

        withdraws_num = len(
                [transaction for transaction in self.__statement.transactions 
                    if transaction['type'] == Withdraw.__name__]
        )
        
        if __value > __limit or withdraws_num >= __withdraw_limit:
            return False
        else:
            return super().withdraw(value)