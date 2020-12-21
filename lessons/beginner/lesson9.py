# -*- coding: utf-8 -*-
"""
1. conversion between types
"""

# conversion

num = 23

print(num, type(num))

float_num = float(num)

print(float_num, type(float_num))

print(int('56'))

a = 9

print(bool(a))
print(bool(0))

if False:
    print('F')

if True:
    print('T')

a = None
if None:
    print('N')

s = ''
if s:
    print('S')

if 'v':
    print('SS')

l = []

if l:
    print('L')

if [1, 2]:
    print('LL')


# these values will always considered as FALSE:
# None, empty string, empty list, empty set, empty tuple, empty dict, 0, and False itself.

# these values will always considered as TRUE:
# non-empty string, non-empty list, non-empty set, non-empty tuple, non-empty dict, any number
# other than 0, and True itself.
