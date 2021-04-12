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
"""
