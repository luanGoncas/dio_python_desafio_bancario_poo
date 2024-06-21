from abc import ABC, abstractmethod
from Accounts import Account

class Transaction(ABC):

    @abstractmethod
    def register(account):
        pass