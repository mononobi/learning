# -*- coding: utf-8 -*-
"""
1. write a function which takes a dict as an input and loops through the
   items of the input dict and returns a new dict of those items that are callable.
   the new dict keys must be the original keys of the input dict and
   the values of new dict must be the generated result of those callables.

   you could use the sample dict below as an input to your function.
"""

import random

from datetime import datetime


def get_current_hour():
    return datetime.now().hour


def get_random_integer():
    return int(random.random() * 100)


sample_dict1 = dict(current_hour=get_current_hour,
                    constant_number=100,
                    random_number=get_random_integer,
                    name='exercise',
                    age=40,
                    current_date=datetime.now,
                    empty=None,
                    a_list=list,
                    another_list=[])

# TODO: Your code goes here:

"""
2. write a function which takes a dict as an input and loops through the
   items of the input dict and converts all keys to upper case and removes
   the original keys and returns the result. note that the original values 
   must be kept as they are after converting keys to upper case.
   
   you could use the sample dict below as an input to your function.
"""

sample_dict2 = dict(name='Jack', Age=23, ADDRESS='Berlin',
                    job='Programmer', Salary=10000,
                    Bank_Account='not specified')

# TODO: Your code goes here:

"""
3. write a function which takes a list of numbers. the list could have duplicate
   values int it. the function must return a list of input items but without any 
   duplication.

   you could use the sample list below as an input to your function.
"""

sample_list3 = [-9, 34, 7, 9, 0, -9, 34, 2, 4, 9, 8, 11, 7, 7, -34, 9, 30]

# TODO: Your code goes here:

"""
4. write a function which takes a list and a set of numbers as input and 
   returns a boolean value. the function must return True if the input list 
   and set are containing the same numbers. note that the order of numbers
   may be different in the list and set.

   you could use the sample lists and sets below as an input to your function.
"""

sample_list4_equal = [9, 1, 0, 5, 6, 8, 3, 2, 4, 7]
sample_set4_equal = {0, 9, 8, 7, 6, 1, 2, 3, 4, 5}

sample_list4_not_equal = [9, 1, 0, 5, 6, 2, 4, 7]
sample_set4_not_equal = {0, 9, 8, 7, 6, 1, 2, 3}

# TODO: Your code goes here:

"""
5. write a function which takes a dict and another single value as key name.
   if the provided key name is present in the input dict, it must return the value
   of that key from dict, otherwise it must return a message telling the key is 
   not present.

   you could use the sample dict below as an input to your function.
"""

sample_dict5 = dict(name='Cameron', age=50, unit='dev',
                    time=datetime.now(), hour=get_current_hour(),
                    random_num=get_random_integer(), empty=None)

# TODO: Your code goes here:

"""
6. write a function which takes two lists as an input.
   it must return the list of values which are present in both lists.

   you could use the sample lists below as an input to your function.
"""

sample_list6_1 = [100, 200, 300, 400, 500, 600, 700, 800]
sample_list6_2 = [100, 150, 200, 250, 300, 250, 350, 400]

sample_list6_3 = ['rabbit', 'lion', 'goat', 'mouse', 'cat', 'wolf']
sample_list6_4 = ['lion', 'bird', 'elephant', 'Rabbit', 'deer', 'snake', 'rabbit']

# TODO: Your code goes here:
