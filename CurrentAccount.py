import Account

class CurrentAccount(Account):
    def __init__(self, balance, number, client, agency, statement, limit, withdraw_limit):
        super().__init__(balance, number, client, agency, statement)
        self.__limit = limit
        self.__withdraw_limit = withdraw_limit
    
    def withdraw(self, value) -> bool:
        __balance = self.__balance or 0
        __value = value or 0
        __limit = self.__limit or 0
        __number = self.__number or 0
        __withdraw_limit = self.__withdraw_limit or 0
        
        if __balance - __value < 0 or __value > __limit or __number > __withdraw_limit:
            return False
        else:
            self.__balance = __balance - __value
            return True