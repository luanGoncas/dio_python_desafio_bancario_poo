# from Users.Client import Client
from Transactions.Statement import Statement

class Account:
    def __init__(self, balance: float, number: int, client, agency: str, 
                 statement: Statement) -> None:
        self.__balance = balance
        self.__number = number
        self.__agency = agency
        self.__client = client
        self.__statement = Statement()
    
    @property
    def balance(self):
        return self.__balance or 0
    
    @property
    def number(self):
        return self.__number or 0
    
    @property
    def agency(self):
        return self.__agency or ''
    
    @property
    def client(self):
        return self.__client or None
    
    @property
    def statement(self):
        return self.__statement or None
    
    @classmethod
    def create_account(cls, client, number: int):
        __balance = 0
        __agency = '0001'
        __statement = None

        return cls(__balance, number, client, __agency, __statement)
    
    @balance.setter
    def withdraw(self, value: float) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        
        if __balance - __value < 0 or __value < 0:
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