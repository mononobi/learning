def sum(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):

    if num2 is None or num2 == 0:
        raise Exception('Divided by null or zero.')

    return num1 / num2


def complex(num1, num2, num3):

    if num3 is None or num3 == 0:
        raise Exception('Divided by null or zero.')

    return (num1 + num2) / num3


# conditions priority
def condition_check(num1, num2, num3):
    if (num1 is not None and num2 is not None) or num3 == 0:
        pass

# condition: if, while

# if condition:
var = 1

# ech section name in if condition is a BRANCH.
# first condition that have been met, execution ends.
if var == 0:
    print('Zero')
elif var != 1:
    print('One')
else:
    print(var)

# each branch will be executed separately.
if var == 0:
    print('Zero')

num1 = 1
num2 = 2

print(num1 is num2)
print(num1 is not num2)
print(num1 == num2)

if var == 1:
    print('One')

# None type:

var = None

if var is None:
    pass


def divide_old(num1=None, num2=None):
    return num1 / num2

# AND


if num1 == 0 and num2 == 3:
    pass

# OR

if num1 == 0 or num2 == 3:
    pass

# collection

# [list], {dict}, {set}, (tuple)

my_list = []

# if collection is not empty, the branch will be executed:
if my_list:
    pass

null_value = None

# if value is not None, the branch will be executed:
if null_value:
    pass

# will always succeed.
if True:
    pass

print(divide(10, 10))


# definition of variables

a = 1
b = 1
c = 1

a1 = b2 = c3 = 1


# WHILE condition

my_var = True
my_false = False
number = 1

# True, False and None must be compared using 'is' instead of '=='.
while number <= 10 and my_var is True:
    number = number + 1
    if number < 4:
        # continue just breaks the current loop and jumps to start of the next loop.
        continue

    number = number + 2
    if number >= 7:
        # ends the loop and exits.
        break

print(number)
