import datetime
from Accounts.Account import Account
from Accounts.CurrentAccount import CurrentAccount
from Transactions.Deposit import Deposit
from Transactions.Statement import Statement
from Transactions.Transaction import Transaction
from Transactions.Withdraw import Withdraw
from Users.Client import Client
from Users.PhysicalPerson import PhysicalPerson

def create_client(client_address: str) -> Client:
    try:
        return Client(address=client_address, accounts=[])
    except Exception as e:
        return f'Invalid Client Creation! str{e}'

def create_physical_person_client(client_address: str, client_cpf: str, 
                                  client_name: str, client_birthdate: datetime) -> PhysicalPerson:
    try:
        return PhysicalPerson(address=client_address, accounts=[], cpf=client_cpf,
                              name=client_name, birthdate=client_birthdate)
    except Exception as e:
        return f'Invalid Physical Person Client Creation! {str(e)}'

def create_account(account_client: Client, client_number: int) -> Account:
    try:
        return Account.create_account(client=account_client, number=client_number)
    except Exception as e:
        return f'Invalid Account Creation! {str(e)}'

def create_current_account(current_account_client: Client,
        client_number: int) -> CurrentAccount:
    try:
        return CurrentAccount.create_account(client=current_account_client,
                                                    number=client_number)
    except Exception as e:
        return f'Invalid Current Account Creation! {str(e)}'

def menu():
    return """
            [1] Deposit
            [2] Withdraw
            [3] Statement
            [4] Create Client
            [5] Create Current Account
            [6] List Clients
            [7] List Current Accounts
            [8] Quit

    => """
# new_client = create_client('Avenida Paulista')
# new_person_client = create_physical_person_client('Avenida Maruipe', '16021242726', 'Luan', '11/04/1995')
# new_account = create_account(new_client, 1)
# new_account2 = create_account(new_person_client, 2)
# new_current_account = create_current_account(new_person_client, 3)

# print('New Client:', new_client)
# print('New Person Client:', new_person_client)
# print('New Account:', new_account)
# print('New Account 2:', new_account2)
# print('New Current Account:', new_current_account)

def main():
    clients = []
    accounts = []

    while True:
        option = menu()