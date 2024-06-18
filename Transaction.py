from abc import ABC, abstractmethod
import Account

class Transaction(ABC):

    @abstractmethod
    def register_account(account):
        pass