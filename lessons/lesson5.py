# -*- coding: utf-8 -*-
"""
str class.
"""

str

value = 'JaCK waldon'

converted = value.capitalize()

print(value, converted)
print(value.casefold())


# center will pad string from both ends.
value2 = 'JaCK waldon'
value2 = value2.center(40)

# rjust() and ljust() are the same as center but will pad from right and left respectively.

print(value2)
print(len(value2))


# number of specified char in a string.
print('COUNT:', value.count('a'))
print('COUNT:', value.count('a', 3, 50))

# gets the lowest index of specified char in a string. -1 if not found.
# index is the same as find but raises an error if value not found.
print('FIND:', value.find('a'))
print('FIND:', value.find('a', 3, 50))

# value.index('lack')

car_find = 'carpool'
print('FIND SUBSTR:', car_find.find('pool'))

# getting a character in specified index.
sixth_char = value[5]
print('SIXTH:', sixth_char)


# string object is also a SEQUENCE.
for char in value:
    print(char)

# string concatenation:
a = 'Sheida'
b = 'Nobakht'

fullname = a + ' ' + b
print('FULLNAME:', fullname)


value = 'JaCK waldon'

print(value.startswith('JaCK'))
print(value.startswith('j'))

# endswith is similar to startswith() but operates on the end of string.

# strip() is equivalent to sql trim.
# lstript and rstrip are the same as strip for left and right.
# by default it removes spaces. but it could be customized.

z = '...ali......'
print('STRIP:', z.strip('.'))
print('LEFT STRIP:', z.lstrip('.'))
print('RIGHT STRIP:', z.rstrip('.'))


# fill with zero to a specified length.
hour = '1'
print('ZFILL:', hour.zfill(4))
