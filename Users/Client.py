# from Accounts.Account import Account
# from Transactions.Transaction import Transaction

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

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.__accounts.append(account)
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {
            ' | '.join(
                [f'{key} = {value}' for key, value in self.__dict__.items()]
            )
        }'