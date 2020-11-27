# -*- coding: utf-8 -*-
"""
1. callable
2. dictionary
3. set
"""


def go():
    pass

# every function and class is callable.
go()
tuple([1, 2, 3])

c1 = callable(go)
c2 = callable(tuple)
c3 = callable(23)
c4 = callable(go())
print(c1, c2, c3, c4)

a = go
b = tuple
a()
print(callable(a))

# dictionary
var0 = {}
var00 = {'name': 'home', 'age': 55, 'name': 'ali'}
var1 = dict()
var2 = dict(name='home', age=23)
print(var1, var0)
print(var2, var00)

# if key does not existed, it raises an error.
name = var2['name']
print(name)

# get does not raise error if key is not present, it returns None or specified default value.
name1 = var2.get('name')

name2 = var2.get('name2', 66)
print(name2)

var00.clear()
print(var00)

# get the list of all dict keys.
print(var2.keys())

for key in var2.keys():
    value = var2.get(key)
    print(key)

for value in var2.values():
    print(value)

for key, value in var2.items():
    print(key, value)

# how to add new keys or update existing keys.
var2['new'] = 90
var2['age'] = None
var2.update(new=80, extra='hi')
print(var2)

var2.update(var00)
var2.update(**var00)

# ** is for unpacking a dict.
# * is for unpacking a sequence (list, set, tuple).

# check if a key exists in a dict
if 'age' in var2:
    print('Yes Key')

if 'age' in var2.keys():
    print('Yes Key')

if None in var2.values():
    print('Yes Value')


# get the value of given key, if key is not present it raises
# an error or returns the default value.
dictionary = dict(address='Tehran', name='Home')
print(dictionary)
address = dictionary.pop('address')
print(address)
print(dictionary)

address = dictionary.pop('not_present', 'US')
print(address)

# set a key in dict if its not already available.
# dictionary['address'] = 'Hamburg'
dictionary = dict(address='Tehran', name='Home')
dictionary.setdefault('address', 'Hamburg')
dictionary.setdefault('age', 4)
print(dictionary)

# remove a key from dict, raises error if key does not exist.
del dictionary['age']

# get count of all keys.
length = len(dictionary)
print(length)

# remove an item from a dict.
# if you provide a default value, .pop does not raise error on not present keys.
dictionary.pop('not_present', 'US')

# if you're sure the key exists:
del dictionary['address']


# set

my_set = set()
my_set3 = {1, 2, 3}
my_set2 = set([1, 2, 3])

# generate a set from a dict keys.
dict_set = set(dictionary.keys())

# add item into set
my_set3.add(55)
print(my_set3)

my_set2.clear()
print(my_set2)

# removes the item in zero index and gets it.
print(my_set3)
print(my_set3.pop())
print(my_set3)

# raises an error is set is empty
# my_set.pop()
print(my_set3)

# remove item from set with its value.
my_set3.remove(2)
print(my_set3)

present = 2 in my_set3
print(present)

# get count of items in a set.
length = len(my_set3)

# indexing is not supported on sets
# a = my_set3[0]

# set item are always unique.
nums = {1, 2, 3, 4, 5, 1, 2, 3}
print(nums)

nums1 = {1, 2, 3, 4, 5}
nums2 = {4, 5, 6, 7, 8}

sub_num1 = {1, 2, 3}

intersection = nums1.intersection(nums2)
print(intersection)

union = nums1.union(nums2)
print(union)

difference = nums1.difference(nums2)
print(difference)

difference = nums2.difference(nums1)
print(difference)


is_subset = sub_num1.issubset(nums1)
print(is_subset)

is_subset = nums1.issubset(sub_num1)
print(is_subset)


is_superset = sub_num1.issuperset(nums1)
print(is_superset)

is_superset = nums1.issuperset(sub_num1)
print(is_superset)

