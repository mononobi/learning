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

account_info: Dict[str, int] = {'acnt': 0, 'slug': 0, 'Balance': 0}
#print(account_info)



# checks if the entry is an integer (for example for a chosen account number by the user)
def check_integer(num):
    if not isinstance(num, int):
        raise Exception('Invalid Number.')
    #except Exception as some_error:
    #    return some_error
    #finally:
    #    print(num)
    return num


#print(check_integer('a'))
#print(check_integer(2))


# will check the length of the account number (IF chosen by the user)
def check_acnt(account):
    if account < 10000 or account > 99999:
        raise Exception('Account number must have 5 digits')
    #except Exception as the_error:
    #    return the_error
    return account


#print(check_acnt(10002))
#print(check_acnt(10))
#print(check_acnt(1000200000))


# generate a hashed password (first version)
#def generate_slug(n1=10000, n2=99999):
#    rand = random_number(n1, n2)
#    output = abs(hash(str(rand))) % (10 ** 8)
#    return output//
#  #int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
# print(generate_slug())


# generate a hashed password (second version)
def slug_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#print(slug_generator())


# generates a hashed random number as a 5-digits account number (IF account number not chosen by the user)
def acnt_generator(n1=10000, n2=99999):
    random.seed()
    rand = random.randrange(n1, n2)
    output = abs(hash(str(rand))) % (10 ** 5)
    return output


#print(acnt_generator())


def open_account(act=0, n1=10000, n2=99999):
    if act != 0:
        check_integer(act)
        check_acnt(act)
        account_info['act'] = act
    else:
        act = acnt_generator(n1, n2)
    slg = slug_generator()
    return act, slg


#print(open_account(44000))
#print(open_account())


def deposit(amount):
    bal = account_info['Balance']
    check_integer(amount)
    new_bal = bal + amount
    account_info.update({'Balance': new_bal})
    return new_bal


print(deposit(20))
print(account_info['Balance'])


print(deposit(50))
print(account_info['Balance'])


#def withdraw(amount):
 #   bal = account_info['Balance']
  #  try:
   #     if bal < amount:
    #        output = num1 - num2
     #   return num1 - num2

def balance():
    return account_info['Balance']


#signs = {'+': deposit, '-': withdraw, 'B': balance}
#account_operations = {}