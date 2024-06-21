from Accounts import Account
import Transaction

class Client:
    def __init__(self, address, accounts) -> None:
        self.__address = address
        self.__accounts = accounts
        pass
    
    @property
    def address(self):
        return self.__address or ''

    @property
    def accounts(self):
        return self.__accounts or []

    def make_transaction(account, transaction): pass

    @accounts.setter
    def add_account(self, account):
        __accounts = self.__accounts or []
        __account = account or None
        self.__accounts.append(__account)