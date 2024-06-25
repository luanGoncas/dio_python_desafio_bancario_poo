import Client
import datetime

class PhysicalPerson(Client):
    def __init__(self, address: str, accounts: list, cpf: str, name: str, birthdate: datetime):
        super().__init__(address, accounts)
        self.__cpf = cpf
        self.__name = name
        self.__birthdate = birthdate