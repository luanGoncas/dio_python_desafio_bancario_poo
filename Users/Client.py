from Accounts import Account
from Transactions import Transaction

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

    def make_transaction(account: Account, transaction: Transaction): pass

    @accounts.setter
    def add_account(self, account: Account):
        __accounts = self.__accounts or []
        __account = Account.create_account(account) or None

        self.__accounts.append(__account)