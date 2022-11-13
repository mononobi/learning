# -*- coding: utf-8 -*-
"""
we have a list of first names and another list of last names.

1. write a concatenate method to loop through the list with fewer items
   and concatenate each first name to last name of the same index, the
   loop must be ended when the shorter list is exhausted.
2. write a method to print the list with maximum length.
3. write a method to sort the first_names ascending and last_names descending.
"""

## Q: why a method? isnt it a function?

first_names = ['azin', 'tarek', 'sheida', 'mohamad',
               'shiva', 'faeze', 'saleh', 'andy', 'reza', 'abi', 'azin']

last_names = ['kamali', 'krohn', 'nobakht', 'nobakht', 'roostaei', 'fallah', 'noorian']


full_names = []
i = 0

if len(first_names) < len(last_names):
    for first_name in first_names:
        full_name = f"{first_name.title()} {last_names[i].title()}"
        full_names.append(full_name)
        i += 1

else:
    for last_name in last_names:
        full_name = f"{first_names[i].title()} {last_name.title()}"
        full_names.append(full_name)
        i += 1

for full_name in full_names:
    print(full_name)