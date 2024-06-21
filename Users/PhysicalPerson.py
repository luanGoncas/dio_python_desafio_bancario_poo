import Client

class PhysicalPerson(Client):
    def __init__(self, address, accounts, cpf, name, birthdate):
        super().__init__(address, accounts)
        self.__cpf = cpf
        self.__name = name
        self.__birthdate = birthdate