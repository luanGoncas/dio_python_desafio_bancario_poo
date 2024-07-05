from datetime import datetime
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

    [1] Current Account Deposit
    [2] Current Account Withdraw
    [3] Current Account Statement
    [4] Create Client
    [5] Create Current Account
    [6] List Clients
    [7] List Current Accounts
    [8] Quit

    => """

    return input(textwrap.dedent(menu))

def create_physical_person_client(clients_list: list) -> str:
    try:
        client_cpf = input('Please, inform the new client\'s CPF: ')
        
        if len(client_cpf) != 11 or not client_cpf.isdecimal():
            raise Exception('Invalid CPF!')

        if any(client.cpf == client_cpf for client in clients_list):
            raise Exception('Client already registered!')

        client_address = input('Please, inform the new client\'s address: ')
        client_name = input('Please, inform the new client\'s name: ')
        client_birthdate = input('Please, inform new the client\'s birthdate (dd/mm/yyyy): ')

        valid_client_birthdate = datetime.strptime(client_birthdate, '%d/%m/%Y').date()

        new_client = PhysicalPerson(
            address=client_address, accounts=[],
            cpf=client_cpf,
            name=client_name,
            birthdate=valid_client_birthdate
        )

        clients_list.append(new_client)
        return f'New Physical Person Client created! {new_client}'
    except Exception as e:
        return f'Invalid Physical Person Client Creation! {str(e)}'

def create_current_account(clients_list: list, accounts_list: list):
    try:
        client_cpf = input('Please, inform the client\'s CPF: ')
        
        if len(client_cpf) != 11 or not client_cpf.isdecimal():
            raise Exception('Invalid CPF!')

        new_account_client = next(
            (client for client in clients_list if client.cpf == client_cpf),
            False
        )
                
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

def post_deposit_operation(clients_list: list) -> str:
    try:
        client_cpf = input('Please, inform the client\'s CPF: ')
        
        if len(client_cpf) != 11 or not client_cpf.isdecimal():
            raise Exception('Invalid CPF!')

        deposit_client = next(
            (client for client in clients_list if client.cpf == client_cpf),
            False
        )

        if not deposit_client:
            raise Exception('Client not found!')
        
        if deposit_client.accounts == []:
            raise Exception('The client informed does not have an account associated with.')
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
            deposit_value = float(input('Inform the deposit value: '))
            deposit_transaction = Deposit(deposit_value)
            deposit_client.make_transaction(deposit_account, deposit_transaction)
            return f'Deposit was successful! {deposit_transaction}'
    except Exception as e:
        return f'Invalid Deposit Operation! {str(e)}'

def post_withdraw_operation(clients_list: list) -> str:
    try:
        client_cpf = input('Please, inform the client\'s CPF: ')

        if len(client_cpf) != 11 or not client_cpf.isdecimal():
            raise Exception('Invalid CPF!')

        withdraw_client = next(
            (client for client in clients_list if client.cpf == client_cpf),
            False
        )

        if not withdraw_client:
            raise Exception('Client not found!')
        
        if withdraw_client.accounts == []:
            raise Exception('The client informed does not have an account associated with.')
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
            previous_transactions = len(withdraw_account.statement.transactions)
            withdraw_value = float(input('Inform the withdraw value: '))
            withdraw_transaction = Withdraw(withdraw_value)
            withdraw_client.make_transaction(withdraw_account, withdraw_transaction)
            current_transactions = len(withdraw_account.statement.transactions)
            if current_transactions > previous_transactions:
                return f'Withdraw was successful! {withdraw_transaction}'
            else:
                raise Exception('Insufficient balance, exceeded limit or daily withdraws')
    except Exception as e:
        return f'Invalid Withdraw! {str(e)}'
    
def get_account_statements(clients_list: list) -> list:
    client_cpf = input('Please, inform the client\'s CPF: ')

    if len(client_cpf) != 11 or not client_cpf.isdecimal():
            raise Exception('Invalid CPF!')

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

def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == '1':
            print(post_deposit_operation(clients))
        elif option == '2':
            print(post_withdraw_operation(clients))
        elif option == '3':
            print(get_account_statements(clients))
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