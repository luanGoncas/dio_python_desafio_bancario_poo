from Accounts.Account import Account
from Users.Client import Client
from Transactions.Statement import Statement
from Transactions.Withdraw import Withdraw

class CurrentAccount(Account):
    def __init__(self, balance: float, number: int, client: Client, agency: str,
                 statement: Statement, limit: float, withdraw_limit: int):
        super().__init__(balance, number, client, agency, statement)
        self.__limit = limit
        self.__withdraw_limit = withdraw_limit
    
    @ classmethod
    def create_account(cls, client, number: int):
        __balance = 0
        __agency = '0001'
        __statement = Statement()
        __limit = 500
        __withdraw_limit = 3

        return cls(__balance, number, client, __agency, __statement, __limit, __withdraw_limit)

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