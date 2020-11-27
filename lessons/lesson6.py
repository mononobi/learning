# -*- coding: utf-8 -*-
"""
1. list
2. tuple
"""

a1 = []
a2 = list()

# list items could be anything and they are not restricted to the same type.
nums = [1, 2, 3, 4, 'name']
print(nums)

# add a single item into a list.
nums.append(6)
print(nums)

nums.clear()
print(nums)

nums = [1, 2, 3, 4, 5, 3, 2, 3, 4]
length = len(nums)
print('LEN:', length)

# get the count of an item in a list. zero if not found.
number_of_occurrences = nums.count(4)
print('COUNT:', number_of_occurrences)
print('COUNT NOT FOUND:', nums.count(48))

# get the first index of an item in a list. raise error if value not found in list.
print('INDEX:', nums.index(3))

# ERROR
# print('INDEX:', nums.index(400000))

# add a range of items into list
b = [100, 200, 300]

# this will add b as a single item into nums.
nums.append(b)
print(nums)

# this will add b's items into nums items one by one.
nums.extend(b)
print(nums)

# insert an item into specified index.
print(nums)
nums.insert(3, 500)
print(nums)

# if index is out of range, it will be added after the last index.
nums.insert(3000, 500)
print(nums)


# get an item in given index and also remove it from the list itself.
item = nums.pop(0)
print(item, nums)

# remove the first occurrence of a value from a list.
# raise error if value not found.
nums.remove(4)
print(nums)


# reverse a list.
n = [1, 2, 3, 4]
n.reverse()
print(n)

n2 = [3, 2, 7, 3, 5, 0]
n2.sort(reverse=True)
print('SORT:', n2)


if 33333 in n2:
    print('YES')
else:
    print('NO')

if 7 in n2:
    print('YES')
else:
    print('NO')

var = 0
if var not in (None, 0):
    r = 3 / var


# the equivalent to a.extend(b)
a = [1, 3]
b = [6, 7]
c = a + b
print(c)


# get the item in specified index.
value = nums[3]
print('GET_INDEX:', value)

# delete an item in specified index.
del nums[2]
print(nums)

print([1, 2] == [2, 1])
print([1, 2] == [1, 2])


# to unpack a sequence of items (list, tuple, set, ...) we set a * at the
# beginning of the value. this is only permitted in method inputs.

values = (1, 2, 3)


def args(*args):
    print(type(args))
    print(args)


args(values)  # not useful.

args(*values)
args(1, 2, 3)


########################################## tuple ##########################################

t1 = ()
t2 = tuple()

# it has some of main list methods:
# len, index, count.
# in, for.

# add two tuples. a + b
# get item at index: a[0]

# non of list modifier methods are available in tuples.


# immutable types: value type: tuple, str, int
# mutable types: reference type: list, dict, set

# mutable types could be changed in-place.
# immutable type could not be changed in-place.

a = (1, 2, 3)
b = a + (4,)
print(b)


a = (1, 2, 3)

a = (1, 2, 3, 4)
print(b)

l = [1, 2]
l.append(4)


def test1(value):
    # this will not change the outer scope value,
    # but the method will see and modify its own value.
    value = [0, 9]
    value.append(33)
    print(value)


value = [1, 2]
test1(value)
print(value)


def test2(value2):
    # this will change the outer scope value2.
    value2.append(33)
    print(value)


value2 = [1, 2]
test2(value2)
print(value2)
