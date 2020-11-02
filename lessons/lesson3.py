# these two imports will import all methods and classes of given module.
import math
import math as a

# these two imports will import the exact requested method or class.
from math import ceil
from math import ceil as base_ceil

import math
import datetime
from math import ceil, factorial


# sample
def my_ceil(num):
    z = a.ceil(num)
    z2 = ceil(num)
    z3 = base_ceil(num)
    return math.ceil(num)


def real_ceil(num):
    return math.ceil(num)


def factor(num):
    ce = real_ceil(num)
    return math.factorial(ce)


print('Ceil 3.7:', real_ceil(3.7))
print('Factorial 5:', factor(4.5))
