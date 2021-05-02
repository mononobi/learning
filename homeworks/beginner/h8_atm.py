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
import math
import string
import hashlib
from typing import Dict
import ast


#account_info: Dict[str, int] = {'acnt': 0, 'slug': 0, 'Balance': 0}
with open("myAccount.txt") as file:  # in read mode, not in write mode, careful
    rd = file.read()
    rd = ast.literal_eval(rd)
account_info = rd


# checks if the entry is an integer (for example for a chosen account number by the user)
def check_integer(num):
    if not isinstance(int(num), int):
        raise Exception('Invalid Number.')
    return int(num)


# will check the length of the account number (IF chosen by the user)
def check_acnt(account):
    if account < 10000 or account > 99999:
        raise Exception('Account number must have 5 digits')
    return account


def check_pass(p):
    if p != account_info['slug']:
        raise Exception('Error: Password is not correct!')
    return 'OK'


# generates a hashed random number as a 5-digits account number (IF account number not chosen by the user)
def acnt_generator(n1=10000, n2=99999):
    random.seed()
    rand = random.randrange(n1, n2)
    output = abs(hash(str(rand))) % (10 ** 5)
    return output


# generate a hashed password
def slug_generator(size=4, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def open_account(act=0, n1=10000, n2=99999):
    if act != 0:
        check_integer(act)
        check_acnt(act)
        account_info['act'] = act
    else:
        act = acnt_generator(n1, n2)
    slg = slug_generator()
    return act, slg


def deposit(dummy=0, amount=0):
    check_integer(amount)
    bal = account_info['Balance']
    new_bal = bal + amount
    account_info.update({'Balance': new_bal})
    return new_bal


def withdraw(pss, amount):
    amount = check_integer(amount)
    check_pass(pss)
    bal = account_info['Balance']
    if bal < amount:
        raise Exception('Balance not sufficient! ')
    new_bal = bal - amount
    account_info.update({'Balance': new_bal})
    return new_bal


def balance(pss, dummy=0):
    check_pass(pss)
    return account_info['Balance']


def get_input_acnt():
    n1 = input('Please choose a 5-digits account number or enter 0 (for an automatic account number allocation): ')
    n1 = check_integer(n1)
    if n1 != 0:
        check_acnt(n1)
    return n1


def get_input_pass():
    n1 = input('Please enter your password: ')
    return check_pass(n1)


operations = {'+': deposit, '-': withdraw, 'b': balance}


def get_input_op():
    n1 = input('Please select the desired operation: "+" for deposit, "-" for withdrawal, "b" for balance: ')
    n2 = input('Please enter the amount (just a 0 if balance): ')
    n2 = check_integer(n2)
    n3 = input('Please enter your password: ')
    return n1, n2, n3

def acnt_operations(op, amnt, pss):
    operation = operations.get(op)
    amnt = check_integer(amnt)
    if operation == None:
        raise Exception('The account operation is unknown!')
    return operation(pss, amnt)

#print(acnt_operations('+', 100, 0))

def finish_all():
    dicti: Dict[str, int] = {'acnt': 0, 'slug': 0, 'Balance': 0}
    with open("myAccount.txt", "w") as file:  # in write mode
        file.write(str(dicti))


def the_messages(msg_type):
    if msg_type == 'n': ## open_account
        message1 = 'Your account number is "{acnt}" and your password is "{pswrd}", please save them for later use.\n'
    elif msg_type == 'b': ## balance
        message1 = 'Your balance is: {blnc} Euro. \n'
    elif msg_type == '+': ## deposit
        message1 = 'The deposit of {amount} Euro is successfully done, your new balance is {blnc} Euro. \n'
    elif msg_type == '-': ## withdraw
        message1 = 'The withdrawal of {amount} Euro is successfully done, your new balance is {blnc} Euro. \n'
    else:
        message1 = 'Operation unknown'
    return message1


def get_command1():
    q = input('Type in "n" to start operations for a new account, otherwise press any other key \n')
    return q


def start_ok(i):
    result = True
    finish_all()
    if i != 'n':
        result = False
    return result


def get_command2():
    q = input('Type in "c" to continue and any other key to finish the operations (all account info willbe deleted) \n')
    return q


def continue_ok(i):
    result = True
    if i != 'c':
        result = False
        finish_all()
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
