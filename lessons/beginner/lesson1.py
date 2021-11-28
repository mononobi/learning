"""
1. basic data types
2. collections
3. function definition and call
"""

# data types: int, str, float, bytes, datetime, date, time, type, bool, None
# collection types: list, tuple, set, dict

# list definition
# in-place
a1 = [1, 2, 3]

# function
a2 = list((1, 2, 3))

# empty
a3 = []

# tuple definition
# in-place
b1 = (1, 2, 3)

# function
b2 = tuple([1, 2, 3])

# set definition
# in-place
c1 = {1, 2, 3}

# empty
c2 = set()

# dictionary definition
# in-place
d1 = {'age': 10, 'name': 'ali'}

# function
d2 = dict(age=10, name='ali')

# empty
d3 = {}


# function definition
# args is always a tuple
def multiple(num1, num2, *args, num3=3, num4=4, **kwargs):
    # getting the item at last index (10):
    x1 = args[2]
    print(x1)

    # getting items by unpacking the tuple
    # the left side items must always be as much as the args items
    a, b, c = args
    print(a, b)

    return num1 * num2


# function call
result = multiple(2, 4, 6, 8, 10, num3=11)

print(result)
