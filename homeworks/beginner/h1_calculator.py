# -*- coding: utf-8 -*-
"""
define four main functions:

1. add: which takes two required arguments.
2. subtract: which takes two required arguments.
3. divide: which takes two required arguments.
4. multiply: which takes two required arguments.

define a calculator function which takes two required numbers and an
optional string operator. if operator is not provided, it must be
considered as 'add'.
calculator function must return the result of each operation.
then you should print the result of calculator method.
"""


def add_func(num1, num2):
    """This will return sum of two provided numbers"""
    return num1 + num2


def subtract_func(num1, num2):
    """This will return subtraction of second number from first number"""
    return num1 - num2


def divide_func(num1, num2):
    """This will return division of first number by second number"""
    try:
        return num1 / num2
    except:
        print('put non-zero second number, next time.')


def multiply_func(num1, num2):
    """This will return sum of two provided numbers"""
    return num1 * num2


def calculator_func(num1, num2, operator='a'):
    """Using the requested operator the result of two numbers will be provided.This calculator will choose the
    operation by third argument:
    a: add
    b: subtraction
    c: division
    d: multiply"""
    if operator == 'b':
        result = subtract_func(num1, num2)
    elif operator == 'c':
        result = divide_func(num1, num2)
    elif operator == 'd':
        result = multiply_func(num1, num2)
    else:
        result = add_func(num1, num2)
    return result

print(calculator_func(1,0,'c'))

print(calculator_func(3,2))
