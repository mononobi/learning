# -*- coding: utf-8 -*-
"""
a simple calculator app.
"""

def sumi(num1, num2):
    return num1 + num2

def minusi(num1, num2):
    return num1 - num2

def divi(num1, num2):
    return num1 / num2

def mulp(num1, num2):
    return num1 * num2

signs = {'+': sumi, '-': minusi, '/': divi, '*': mulp}

def calci(num1, num2, sign):
    operation = signs.get(sign) # dict.get rerurns NONE if the key does not exist
    if operation is None:
        raise Exception('Operation is not defined')
    return operation(num1, num2)

def check_int(num):
    if not num.isdigit():
        raise Exception('The number is not valid')
    return int(num)

def get_input():
    num1 = input('Please enter the first number: ')
    num2 = input('Please enter the second number: ')
    sign = input('Please enter one of the basic four operations: ')
    num1 = check_int(num1)
    num2 = check_int(num2)
    return num1, num2 , sign   ## it would return a tuple then

if __name__ == '__main__':
    while True:
        try:
            numi1, numi2, signi = get_input()
            result = calci(numi1, numi2, signi)
            print(result)
        except Exception as err:
            print(err)





