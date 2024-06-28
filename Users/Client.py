from Accounts.Account import Account
from Transactions.Transaction import Transaction

class Client:
    def __init__(self, address: str, accounts: list) -> None:
        self.__address = address
        self.__accounts = accounts
        pass
    
    @property
    def address(self):
        return self.__address or ''

    @property
    def accounts(self):
        return self.__accounts or []

    def make_transaction(self, account: Account, transaction: Transaction):
        transaction.register(account)

    @accounts.setter
    def add_account(self, account: Account):
        __account = Account.create_account(account) or None

        self.__accounts.append(__account)
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}'