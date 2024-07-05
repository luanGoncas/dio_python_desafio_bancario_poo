# Modelando o Sistema Bancário em POO com Python

## Overview

Este repositório contém a implementação do desafio da DIO, o de um sistema bancário simples representado pelo diagrama de classes fornecido abaixo. O objetivo deste sistema é gerenciar contas bancárias, transações e clientes de forma organizada e eficiente. O diagrama de classes descreve a estrutura e os relacionamentos entre diferentes entidades no sistema, incluindo contas, transações e clientes. Ele é uma versão modificada do diagrama fornecido na especificação do desafio, já que é mais
condizente com a impelmentação final.

![Diagrama de Classes](/Diagrama%20Bancario.drawio.png)

O diagrama de classes fornecido define as seguintes classes e seus relacionamentos:

### Classes Principais

1. **Account (Conta)**
   - Atributos:
     - `balance`: float
     - `number`: int
     - `agency`: str
     - `client`: Client
     - `statement`: Statement
   - Métodos:
     - `balance()`: float
     - `number()`: int
     - `agency()`: str
     - `client()`: Client
     - `statement()`: Statement
     - `create_account(client, number)`: Account
     - `withdraw(value)`: bool
     - `deposit(value)`: bool

2. **CurrentAccount (Conta Corrente)**
   - Herda de: `Account`
   - Atributos:
     - `limit`: float
     - `withdraw_limit`: int

3. **Statement (Extrato)**
   - Atributos:
     - `transactions`: list
   - Métodos:
     - `transactions()`: list
     - `add_transaction(transaction)`: Transaction

4. **Transaction (Transação)**
   - Interface com os seguintes métodos:
     - `value()`: float
     - `register(account)`: Account

5. **Deposit (Depósito)**
   - Implementa: `Transaction`
   - Atributos:
     - `value`: float
   - Métodos:
     - `value()`: float
     - `register(account)`: Account

6. **Withdraw (Saque)**
   - Implementa: `Transaction`
   - Atributos:
     - `value`: float
   - Métodos:
     - `value()`: float
     - `register(account)`: Account

7. **Client (Cliente)**
   - Atributos:
     - `address`: str
     - `accounts`: list
   - Métodos:
     - `address()`: str
     - `accounts()`: list
     - `make_transaction(account, transaction)`: Transaction
     - `add_account(account)`: Account

8. **PhysicalPerson (Pessoa Física)**
   - Herda de: `Client`
   - Atributos:
     - `cpf`: str
     - `name`: str
     - `birthdate`: datetime
   - Métodos:
     - `cpf()`: str
     - `name()`: str
     - `birthdate()`: str