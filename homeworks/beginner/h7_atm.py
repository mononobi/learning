# -*- coding: utf-8 -*-
"""
we want to implement a simple ATM in this homework.

the ATM has these main operations:

1. register: register a new account. it should assign a number as
             account number and a slug as access key to the account.
             after creation of each account, the account number and the access
             key must be printed to the user.

2. deposit: deposit some cash to specified account.

3. withdraw: withdraw some cash from an account, this needs the access key
             to be provided by user.
             if the balance is not enough, it must inform the user.

4. balance: view the balance of an account, this needs the access key
            to be provided by user.

* after each operation, the ATM should wait for another command from the user.
* the ATM state must remain in memory as long as the app is running.
"""

from random import randint

# accounts created in the program and their data are stored in this dictionary:
accounts_storage = dict()
# Starting point for accounts number serial:
account_serial = 1
account_start = 1000


class NotIntPositiveError(Exception):
    """This is to distinguish invalid input in various functions."""


def register_account():
    """This opens an accounts and prints account number and access key. access key is required for some banking
        operations."""

    global account_serial
    # Q: why I cant use account_serial assignment locally? comment last line to see

    account_balance = 0
    # A simple way to build account number:
    account_number = account_start + account_serial
    # Access key is built on an insecure way.
    account_key = account_number + randint(0, account_start)
    print(f'\nNew account created. Access key for account number {account_number} is: {account_key}')
    accounts_storage.update({
        account_number: {
            'account_key': account_key,
            'account_balance': account_balance
        }})

    account_serial += 1

    return account_number


def deposit_amount(account_number, amount):
    """gets an integer amount and adds it to the requested account_number"""

    # Q: as convention should parameter defer from local var?

    if account_number in accounts_storage:
        if amount <= 0 or not isinstance(amount, int):

            # Q: Should I raise my exception or catch it on valueError on CALLER(Manager)?

            raise NotIntPositiveError('Amount to deposit must be positive integer.')
        else:
            balance = accounts_storage[account_number]['account_balance']
            balance += amount
            accounts_storage[account_number].update({'account_balance': balance})
            ###############################################################################
            # account_info = accounts_storage[account_number]
            # account_info['account_balance'] = account_info['account_balance'] + amount
            ####### accounts_storage[account_number] = account_info #######################
            ###############################################################################
        return None
    else:
        # meaning account not found:
        return -1


def withdraw_account(account_number, amount, access_key):
    """withdraw an amount from specified account. controls balance and negative amount."""

    if account_number in accounts_storage:
        if amount <= 0 or not isinstance(amount, int):
            raise NotIntPositiveError('Amount to deposit must be positive integer.')
        elif access_key == accounts_storage[account_number]['account_key']:
            balance = accounts_storage[account_number]['account_balance']
            balance -= amount
            if balance >= 0:
                accounts_storage[account_number].update({'account_balance': balance})
                print('Withdraw done.')
            else:
                print('Not enough balance to withdraw.')
        else:
            print('access key not matched.')
        return None
    else:
        # meaning account not found:
        return -1

    # Q: Should I print in function? or return a result to decide in outer code? or another presentation function?
    # Q: This is crucial, for general features like account not found.


def show_balance(account_number):
    """Shows balance of given account number. Does not control access key."""

    if account_number in accounts_storage:
        balance = accounts_storage[account_number]['account_balance']
        print(f'Balance of {account_number} is {balance}.')
        return None
    else:
        # meaning account not found:
        return -1


def run_atm():
    print('Welcome to Saleh ATM!')
    while 1:
        try:
            print(accounts_storage)
            oper = int(input('\nOperations to select from. Press 0 (zero key) to quit.'
                             '\n\tRegister a new account = 1'
                             '\n\tDeposit an amount = 2'
                             '\n\tWithdraw an amount = 3'
                             '\n\tShow balance  = 4'
                             '\n\tPlease select an operation: '))

            if oper == 1:
                register_account()

            elif oper == 2:
                requested_account = int(input('Please enter account number: '))
                requested_amount = int(input('How much do you want to deposit? '))
                if not deposit_amount(requested_account, requested_amount):
                    print('Deposit done.')
                else:
                    print('Not a valid account')

            elif oper == 3:
                requested_account = int(input('Please enter account number: '))
                requested_amount = int(input('How much do you want to withdraw? '))
                requested_access_key = int(input('What is your access key? '))
                result = withdraw_account(requested_account, requested_amount, requested_access_key)
                if result == -1:
                    print('Not a valid account')


            elif oper == 4:
                requested_account = int(input('Please enter account number: '))
                result = show_balance(requested_account)
                if result:
                    print('Not a valid account')

            elif oper == 0:
                break

            else:
                continue

        except ValueError:
            print('please enter correct number.')

        except NotIntPositiveError as error:
            print(error)


d = dict(j=1, b=2, c=3)
for i in sorted(d):
    print(i, d.get(i))

if __name__ == '__main__':
    run_atm()
