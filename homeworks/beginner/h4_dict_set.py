# -*- coding: utf-8 -*-
"""
1. write a function which takes a dict as an input and loops through the
   items of the input dict and returns a new dict of those items that are callable.
   the new dict keys must be the original keys of the input dict and
   the values of new dict must be the generated result of those callables.

   you could use the sample dict below as an input to your function.
"""

# Q: What are these functions?!

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

def make_callable_value_dict(dict1):
    """takes one dictionary and returns a new one with just callable values."""

    new_dict = {}

    for key, value in dict1.items():
        if callable(dict1[key]):
            new_dict.setdefault(key, value())

    print(new_dict)

    return new_dict


print('1st Assignment result:')
make_callable_value_dict(sample_dict1)



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

def convert_keys_uppercase_dictionary(dict1):
    """takes one dictionary and convert keys to uppercase."""
    new_dict = {}

    for key, value in dict1.items():
        new_dict[key.upper()] = value

    print(new_dict)

    return new_dict

print('\n2nd Assignment result:')
convert_keys_uppercase_dictionary(sample_dict2)



"""
3. write a function which takes a list of numbers. the list could have duplicate
   values int it. the function must return a list of input items but without any 
   duplication.

   you could use the sample list below as an input to your function.
"""

sample_list3 = [-9, 34, 7, 9, 0, -9, 34, 2, 4, 9, 8, 11, 7, 7, -34, 9, 30]

# TODO: Your code goes here:

def make_list_unique(list1):
    """takes a list of numbers and returns a new one without duplicate elements."""

    new_list = []

    for element in list1:
        if element not in new_list:
            new_list.append(element)

    print(new_list)

    return new_list


print('\n3rd Assignment result:')
make_list_unique(sample_list3)



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

def check_equality_list_set(list1, set1):
    """takes a list and a set, and evaluates if they are the same."""
    set_of_list = set(list1)
    if set_of_list == set1:
        print('True')
        return True
    print('False')
    return False

print('\n4th Assignment result:')
check_equality_list_set(sample_list4_equal, sample_set4_equal)
check_equality_list_set(sample_list4_not_equal, sample_set4_not_equal)


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

def check_value_in_dict(dict1, value1):
    """takes a dictionary and a value and returns its value"""
    if value1 in dict1.keys():
        return dict1[value1]
    else:
        return f"The value provided ({value1}) is not present in the dictionary."


print('\n5th Assignment result:')
result1 = check_value_in_dict(sample_dict5, 'name')
print(result1)
result2 = check_value_in_dict(sample_dict5, 'not')
print(result2)

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

def make_intersection_of_lists(list1, list2):
    """Takes two lists and returns a list of the same items in both."""
    set1 = set(list1)
    set2 = set(list2)
    new_tuple = set1.intersection(set2)
    return list(new_tuple)

print('\n6th Assignment result:')
print(make_intersection_of_lists(sample_list6_1, sample_list6_2))
print(make_intersection_of_lists(sample_list6_3, sample_list6_4))