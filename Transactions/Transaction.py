from abc import ABC, abstractmethod
from Accounts import Account

class Transaction(ABC):
    @property
    @abstractmethod
    def value(self): pass

    @abstractmethod
    def register(account: Account):
        pass