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

import random
import string

# keys of this dict is each account number.
# each value is another dict.
accounts = {}

# checks if the entry is an integer (for example for a chosen account number by the user)
# THIS IS WRONG:
# def check_integer(num):
#     if not isinstance(int(num), int):
#         raise Exception('Invalid Number.')
#     return int(num)


def get_integer(number):
    try:
        return int(number)
    except ValueError:
        raise Exception('Invalid Number.')


def get_account(account_number):
    if account_number in accounts:
        return accounts.get(account_number)

    raise Exception('Account does not exist.')


# will check the length of the account number (IF chosen by the user)
def check_account(account_number):
    # isdigit() returns a value indicating that all characters of a string are integers.
    if not account_number.isdigit() or len(account_number) != 5:
        raise Exception('Account number must have 5 digits')


def check_password(account_number, password):
    account = get_account(account_number)
    if password != account.get('slug'):
        raise Exception('Error: Password is not correct!')


# generates a hashed random number as a 5-digits account number (IF account number not chosen by the user)
def generate_account_number(size=5):
    number = ''.join(random.choice(string.digits) for _ in range(size))
    # it is shorthand form of: number in accounts.keys()
    if number in accounts:
        number = generate_account_number(size)

    return number


# generate a hashed password
def generate_password(size=4, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def open_account():
    account_number = get_open_account()
    account = {}
    if account_number != '':
        check_account(account_number)
    else:
        account_number = generate_account_number()

    password = generate_password()
    account.update(password=password, balance=0)
    accounts[account_number] = account

    print('\nYour account info is:', account)


def deposit():
    destination_account = get_destination_account()
    amount = get_input_amount()
    account = get_account(destination_account)
    current_balance = account.get('balance')
    new_balance = current_balance + amount
    account.update(balance=new_balance)
    return new_balance


def withdraw():
    destination_account = get_destination_account()
    amount = get_input_amount()
    password = get_input_password()
    account = get_account(destination_account)
    check_password(destination_account, password)
    current_balance = account.get('balance')
    if current_balance < amount:
        raise Exception('Balance is not sufficient! ')

    new_balance = current_balance - amount
    account.update(balance=new_balance)
    return new_balance


def balance():
    destination_account = get_destination_account()
    password = get_input_password()
    account = get_account(destination_account)
    check_password(destination_account, password)
    return account.get('balance')


operations = {'+': deposit, '-': withdraw, 'b': balance, 'n': open_account}


def operate():
    input_operation = get_input_operation()
    operation = operations.get(input_operation)
    if operation is None:
        raise Exception('The operation is unknown!')
    return operation()


def get_open_account():
    account_number = input('Please choose a 5-digits account number or press enter '
                           '(for an automatic account number allocation): ')

    if account_number != '':
        check_account(account_number)

    return account_number


def get_destination_account():
    account_number = input('Please enter the destination account number: ')
    check_account(account_number)
    return account_number


def get_input_amount():
    amount = input('Please input the amount: ')
    amount = get_integer(amount)
    if amount <= 0:
        raise Exception('Incorrect amount.')
    return amount


def get_input_password():
    password = input('Please enter your password: ')
    return password


def get_input_operation():
    operation = input('Please select the desired operation: "+" for deposit, '
                      '"-" for withdrawal, "b" for balance: ')

    return operation


def the_messages(msg_type):
    if msg_type == 'n': ## open_account
        message1 = '\nYour account number is "{acnt}" and your password is "{pswrd}", please save them for later use.\n'
    elif msg_type == 'b': ## balance
        message1 = '\nYour balance is: {blnc} Euro. \n'
    elif msg_type == '+': ## deposit
        message1 = '\nThe deposit of {amount} Euro is successfully done, your new balance is {blnc} Euro. \n'
    elif msg_type == '-': ## withdraw
        message1 = '\nThe withdrawal of {amount} Euro is successfully done, your new balance is {blnc} Euro. \n'
    else:
        message1 = '\nOperation unknown'
    return message1


def get_command1():
    q = input('Type in "n" to start operations for a new account, otherwise press any other key to exist the program.\n')
    return q


def start_ok(i):
    result = True
    if i != 'n':
        result = False
    return result


def get_command2():
    q = input('Type in "c" to continue, or any other key to finish the operations (all account info will be deleted)\n')
    return q


def continue_ok(i):
    result = True
    if i != 'c':
        result = False
    return result


if __name__ == '__main__':
    while start_ok(get_command1()):
        try:
            acnt = get_input_acnt()
            if acnt == 0:
                account_info['acnt'] = open_account()[0]
            else:
                account_info['acnt'] = acnt
            account_info['slug'] = open_account()[1]
            with open("myAccount.txt", "w") as file:  # in write mode
                file.write(str(account_info))
            message = the_messages('n')
            message = message.format(acnt=account_info['acnt'], pswrd=account_info['slug'])
            print(message)
            while continue_ok(get_command2()):
                try:
                    #pss = get_input_pass()
                    #print(pss)
                    op, amnt, pss = get_input_op()
                    acnt_operations(op, amnt, pss)
                    with open("myAccount.txt", "w") as file:  # in write mode
                        file.write(str(account_info))
                    message = the_messages(op)
                    message = message.format(amount=amnt, blnc=account_info['Balance'])
                    print(message)
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)
