from Users import Client
# from Users import PhysicalPerson
from Transactions import Statement

class Account:
    def __init__(self, balance: float, number: int, client: Client, agency: str, 
                 statement: Statement) -> None:
        self.__balance = balance
        self.__number = number
        self.__agency = agency
        self.__client = client
        self.__statement = statement
    
    @property
    def balance(self):
        return self.__balance or 0
    
    @balance.setter
    def withdraw(self, value: float) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        
        if __balance - __value < 0:
            return False
        else:
            self.__balance = __balance - __value
            return True
    
    @balance.setter
    def deposit(self, value: float) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        self.__balance = __balance + __value
        return True

    def create_account(self, client: Client, number: int):
        return Account(0, number=number, client=client, agency='0001', statement=None)