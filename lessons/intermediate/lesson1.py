# -*- coding: utf-8 -*-
"""
1. object oriented concept.
"""


class Account:
    def __init__(self, number):
        self.number = number


# instance or object of a class.
my_account_object = Account(1000)
my_account_object2 = Account(2000)

my_account_class = Account
