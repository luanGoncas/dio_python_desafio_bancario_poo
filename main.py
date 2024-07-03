import datetime
import textwrap
from Accounts.Account import Account
from Accounts.CurrentAccount import CurrentAccount
from Transactions.Deposit import Deposit
from Transactions.Statement import Statement
from Transactions.Transaction import Transaction
from Transactions.Withdraw import Withdraw
from Users.Client import Client
from Users.PhysicalPerson import PhysicalPerson

def menu() -> input:
    menu = """

    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] Create Client
    [5] Create Current Account
    [6] List Clients
    [7] List Current Accounts
    [8] Quit

    => """

    return input(textwrap.dedent(menu))

def create_physical_person_client(clients_list: list) -> str:
    try:
        client_address = input('Please, inform the new client\'s address: ')
        client_cpf = input('Please, inform the new client\'s CPF: ')
        client_name = input('Please, inform the new client\'s name: ')
        client_birthdate = input('Please, inform new the client\'s birthdate (dd/mm/yyyy): ')

        new_client = PhysicalPerson(
            address=client_address, accounts=[],
            cpf=client_cpf,
            name=client_name,
            birthdate=client_birthdate
        )

        clients_list.append(new_client)
        return f'New Physical Person Client created! {new_client}'
    except Exception as e:
        return f'Invalid Physical Person Client Creation! {str(e)}'

def create_current_account(clients_list: list, accounts_list: list):
    try:
        client_cpf = input('Please, inform the client\'s CPF: ')
        new_account_client = False

        for client in clients_list:
            if client.cpf == client_cpf:
                new_account_client = client
                
        if not new_account_client:
            raise Exception('Client not found!')
        
        client_number = len(accounts_list) + 1
        new_account = CurrentAccount.create_account(
            client=new_account_client,
            number=client_number
        )

        accounts_list.append(new_account)
        new_account_client.add_account(new_account)

        return f'New Current Account created! {new_account}'
    except Exception as e:
        return f'Invalid Current Account Creation! {str(e)}'

def post_deposit_operation(clients_list: list) -> None:
    client_cpf = input('Please, inform the client\'s CPF: ')
    deposit_client = next(
        (client for client in clients_list if client.cpf == client_cpf),
        False
    )

    if not deposit_client:
        return 'Client not found!'
    
    if deposit_client.accounts == []:
        return 'The client informed does not have an account associated with.'
    else:
        account_number = int(input('Please, inform the account number: '))
        deposit_account = next(
            (account 
             for account in deposit_client.accounts
               if account.number == account_number),
            False
        )

    if not deposit_account:
        return 'Invalid client number informed...'
    else:
        deposit_value = float(input('Informe the deposit value: '))
        deposit_transaction = Deposit(deposit_value)
        deposit_client.make_transaction(deposit_account, deposit_transaction)

def post_withdraw_operation(clients_list: list) -> None:
    client_cpf = input('Please, inform the client\'s CPF: ')
    withdraw_client = next(
        (client for client in clients_list if client.cpf == client_cpf),
        False
    )

    if not withdraw_client:
        return 'Client not found!'
    
    if withdraw_client.accounts == []:
        return 'The client informed does not have an account associated with.'
    else:
        account_number = int(input('Please, inform the account number: '))
        withdraw_account = next(
            (account 
             for account in withdraw_client.accounts
               if account.number == account_number),
            False
        )

    if not withdraw_account:
        return 'Invalid client number informed...'
    else:
        withdraw_value = float(input('Informe the deposit value: '))
        withdraw_transaction = Withdraw(withdraw_value)
        withdraw_client.make_transaction(withdraw_account, withdraw_transaction)

def get_account_statements(clients_list: list) -> list:
    client_cpf = input('Please, inform the client\'s CPF: ')
    statements_client = next(
        (client for client in clients_list if client.cpf == client_cpf),
        False
    )

    if not statements_client:
        return 'Client not found!'
    
    if statements_client.accounts == []:
        return 'The client informed does not have an account associated with.'
    else:
        account_number = int(input('Please, inform the account number: '))
        statements_account = next(
            (account 
             for account in statements_client.accounts
               if account.number == account_number),
            False
        )
    
    if statements_account.statement.transactions == []:
        return 'The client account does not have any transactions to show!'
    else:
        return [transaction for transaction in statements_account.statement.transactions]

# new_person_client = create_physical_person_client('Avenida Maruipe', '16021242726', 'Luan', '11/04/1995')
# new_current_account = create_current_account(new_person_client, 3)

# print('\n\nNew Person Client:', new_person_client)
# print('\n\nNew Current Account:', new_current_account)

def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == '1':
            post_deposit_operation(clients)
        elif option == '2':
            post_withdraw_operation(clients)
        elif option == '3':
            get_account_statements(clients)
        elif option == '4':
            print(create_physical_person_client(clients))
        elif option == '5':
            print(create_current_account(clients, accounts))
        elif option == '6':
            for client in clients: print(client)
        elif option == '7':
            for account in accounts: print(account)
        elif option == '8':
            break

if __name__ == '__main__':
    main()