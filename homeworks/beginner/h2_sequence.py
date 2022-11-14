# -*- coding: utf-8 -*-
"""
we have a list of first names and another list of last names.

1. write a concatenate method to loop through the list with fewer items
   and concatenate each first name to last name of the same index, the
   loop must be ended when the shorter list is exhausted.
2. write a method to print the list with maximum length.
3. write a method to sort the first_names ascending and last_names descending.
"""

# Q: why a method? isn't it a function? Be cool

first_names = ['azin', 'tarek', 'sheida', 'mohamad',
               'shiva', 'faeze', 'saleh', 'andy', 'reza', 'abi', 'azin']

last_names = ['kamali', 'krohn', 'nobakht', 'nobakht', 'roostaei', 'fallah', 'noorian']


def concat_lists(list1, list2):
    """"gets two lists, first name as first parameter and concatinates their elements, upto the shrter list"""

    full_names = []
    firstname_first = True

    if len(list1) < len(list2):
        smaller_list = list1
        bigger_list = list2
    else:
        smaller_list = list2
        bigger_list = list1
        firstname_first = False

    i = 0

    for smaller_list_item in smaller_list:
        if firstname_first:
            full_name = f"{smaller_list_item.title()} {bigger_list[i].title()}"
            full_names.append(full_name)
            i += 1
        else:
            full_name = f"{bigger_list[i].title()} {smaller_list_item.title()}"
            full_names.append(full_name)
            i += 1

    print(full_names)
    return (full_names)


concat_lists(first_names, last_names)