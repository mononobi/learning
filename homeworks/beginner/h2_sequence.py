# -*- coding: utf-8 -*-
"""
we have a list of first names and another list of last names.

1. write a concatenate method to loop through the list with fewer items
   and concatenate each first name to last name of the same index, the
   loop must be ended when the shorter list is exhausted.
2. write a method to print the list with maximum length.
3. write a method to sort the first_names ascending and last_names descending.
"""

first_names = ['sara', 'joshua', 'shelly', 'david',
               'tilda', 'nicole', 'jack', 'andy', 'joseph', 'zelda', 'price']

last_names = ['otto', 'bellington', 'laswell', 'larson', 'cherry', 'kidman', 'de niro']

############################### FIRST TRY #############################################################################
###### Excersice 1 ######


def get_shorter_list(a, b):
    """gets two lists and returns the shorter one.
     If both are the same length, returns the first list"""
    len_a = len(a)
    len_b = len(b)
    if len_a <= len_b:
        min_list = a
    else:
        min_list = b
    return min_list


# test
print('The shorter list is: ', get_shorter_list(first_names, last_names))


def match_names_v1(a, b):
    """gets two lists and matches the first and last names
     Uses the above method to find the shorter list"""
    ref_list = get_shorter_list(first_names, last_names)
    for index, name in enumerate(ref_list):
        print(index + 1, a[index].capitalize(), b[index].capitalize())


# test
print('Matching by the first version of the function: ')
print(match_names_v1(first_names, last_names))


def match_names_v2(a, b):
    """gets two lists and matches the first and last names
     Finding the right (shorter) indexing happens within the function itself"""
    for index, name in enumerate(a):
        print(index + 1, a[index].capitalize(), b[index].capitalize())
        if index >= min(len(a), len(b)) - 1:
            break


# test
print('Matching by the second version of the function: ')
print(match_names_v2(first_names, last_names))


######  Excersice 2 ######

def get_longer_list(a, b):
    """gets two lists and returns the longer one
     If they are both the same size, returns the first one"""
    max_len = max(len(a), len(b))
    max_list = b
    if len(a) == max_len:
        max_list = a
    return max_list


# test
print('The longer List is: ', get_longer_list(first_names, last_names))


###### Excercise 3 ######
def sort_names1(a, b):
    """sorts the lists
     print the values of the lists one by one"""
    a = sorted(a)
    b = sorted(b, reverse=True)
    print('First names: ')
    for index, firstname in enumerate(a):
        print(index + 1, firstname)
    print('Last names: ')
    for index, lastname in enumerate(b):
        print(index + 1, lastname)


# test
sort_names1(first_names, last_names)


def sort_names2(a, b):
    """sorts the lists
     prints each list as a whole list"""
    a = sorted(a)
    b = sorted(b, reverse=True)
    return a, b


# test
print(sort_names2(first_names, last_names))


############################### SECOND TRY ############################################################################


def check_length(a, b, c='max'):
    result = b
    if c == 'min':
        if len(a) < len(b):
            result = a
    else:
        if len(a) > len(b):
            result = a
    return result


print(check_length(first_names, last_names))


def match_names_v3(a, b):
    mini = check_length(a, b, c='min')
    for index, names in enumerate(mini):
        print(index+1, a[index], b[index])


print(match_names_v3(first_names, last_names))

import random
print(random.randrange(10, 12))
