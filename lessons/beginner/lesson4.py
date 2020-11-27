# -*- coding: utf-8 -*-
"""
1. for loop
2. mathematical operators
3. boolean type
"""

# all mathematical operators:
# +, -, *, /
# **: power, %: remaining

# loop:
# for, while

# for

cars = ['BMW', 'BENZ', 'TOYOTA']
cars_tuple = ('BMW', 'BENZ', 'TOYOTA')

# simple indexing (not recommended)
index = 0
for name in cars:
    print(name, index)

    index = index + 1
    # go to next loop and ignore the below code.
    if True:
        continue

    # end the whole loop and do not execute anymore loops.
    if True:
        break


# correct indexing
# enumerate returns a tuple of two items, so we should unpack it.
# instead of writing: 'value = enumerate()', we write 'index, value = enumerate()'.
for index, name in enumerate(cars):
    print(name, index)

    # go to next loop and ignore the below code.
    if True:
        continue

    # end the whole loop and do not execute anymore loops.
    if True:
        break


# looping through a range of numbers.
# range(start, end, step)
# start is inclusive, end is exclusive.
for index in range(3, 11, 2):
    print('RANGE')
    print(index)

# returns the count of all items in a sequence.
length = len(cars_tuple)
print('LENGTH', length)
print('LENGTH', len([]))

# min and max in a sequence. all items must be from the same type.
print(max(cars))
print(max(10, 20, 30))

# str and repr does the same thing by default. converting anything to string.
print(str(10))
print(repr(10))


# power a ^ 3
# two ways.
value1 = 3 ** 2
value2 = pow(3, 2)

print(value1, value2)

# sorting sequences. all items must be from the same type.
my_list = [8, 3, 5, 4.5]

# to sort descending, set reverse=True.
# default is ascending.
sorted_list = sorted(my_list, reverse=False)
print('SORTED:', sorted_list)

# converting to int:
value1 = int('45')
value2 = int(6.7)
value3 = int(8)

print('INT:', value1, value2, value3)

# float conversion:
value_float1 = float('4')
value_float2 = float('4.7')
value_float3 = float(5)

print('FLOAT:', value_float1, value_float2, value_float3)

# boolean
value_true = bool(-3)
value_false = bool(0)
print(value_true, value_false)

# remaining of division.
value = 8 % 6
print('REMAINING', value)

print('A' * 1000)
