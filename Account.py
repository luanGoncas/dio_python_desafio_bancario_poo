import Client

class Account:
    def __init__(self, balance, number, client, agency, statement) -> None:
        self.__balance = balance
        self.__number = number
        self.__agency = agency
        self.__client = client
        self.__statement = statement
        pass
    
    @property
    def balance(self):
        return self.__balance or 0
    
    @balance.setter
    def withdraw(self, value) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        
        if __balance - __value < 0:
            return False
        else:
            self.__balance = __balance - __value
            return True

    
    @balance.setter
    def deposit(self, value) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        self.__balance = __balance + __value
        return True

    def create_account(self, client, number) -> Client:
        
        pass