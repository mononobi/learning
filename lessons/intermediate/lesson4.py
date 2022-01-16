# -*- coding: utf-8 -*-
"""
1. magic methods
2. hashing
"""

a = 1
b = 2
sum = a + b
sum = a.__add__(b)
print(sum)

ab = abs(sum)
ab = sum.__abs__()


boo = bool(sum)
boo = b != 2
sum.__bool__()

# equality by value
equal = a == b
equal = a.__eq__(b)

z = 54
f = 54


my_h = hash(5.5)
print(my_h)

my_h = a.__hash__()

int
class Test:
    def __init__(self, name='p1'):
        self._name = name

    def __eq__(self, other):
        if not isinstance(other, Test):
            return False

        if self._name == other._name:
            return True

        return False

    def __hash__(self):
        # when we override __eq__, we need to override __hash__
        # to unify the behavior on equality check.
        return hash(self._name)

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self) + super().__repr__()


print(hash(Test))
print(hash(Test()))

print(id(Test))
print(id(Test()))

a = Test()
b = Test()

# id gets the memory address of a variable.

print(id(a))
print(id(b))
print(a is b)
print(a == b)

# '==' used for equality check by value
# 'is' used for equality check by reference (memory address of variables)

# on primitive types, equality by value will work out of the box.
# on primitive types, equality by reference will work as if it was checked by value.
# print(9999999999999 is 9999999999999)
print(9999999999999 == 9999999999999)

# on custom types (your classes), equality by value will not work out of the
# box and delegates to equality by reference.
# on custom types (your classes), equality by reference will work out of the box.
a = Test()
b = Test()

print(a is b)
print(a == b)

a = Test('p1')
b = Test('p2')
print(a == 1)
print(a == b)

a = Test('p2')
b = Test('p2')
print(a == b)
print(a is b)
print(hash(a), hash(b))
print(id(a), id(b))

# repr and str give the string representation of a value. they are the same by default but,
# they can be changed by overriding __repr__ and __str__ in our classes.
my_l = [a]
print(str(a))
print(repr(a))

# some primitive types (int, float, bool) are hashable.
# immutable types are hashable (tuple, str, type).

# custom types are hashable if you don't override __eq__, __ne__, otherwise
# you must override the __hash__ itself.

# mutable types are NOT hashable (list, dict, set).

# hashable means they have implemented __hash__ in their class.

# unhashable means they have NOT implemented __hash__ in their class.

# dict keys must be hashable.

# this will:
dm = {(): 1}

# this won't work
# di = {[]: 1}
