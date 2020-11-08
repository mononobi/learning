# -*- coding: utf-8 -*-

#define four main functions:

#1. add: which takes two required arguments.
#2. subtract: which takes two required arguments.
#3. divide: which takes two required arguments.
#4. multiply: which takes two required arguments.

#define a calculator function which takes two required numbers and an
#optional string operator. if operator is not provided, it must be
#considered as 'add'.
#calculator function must return the result of each operation.
#then you should print the result of calculator method.


def sum(num1, num2):
    return(num1+num2)

def sub(num1, num2):
    return(num1-num2)

def div(num1, num2):
    if num2 is None or num2==0:
        raise('Cannot be divided by Zero!!!')
    return(num1/num2)

def mul(num1, num2):
    return(num1*num2)

#print(mul(1,3))

def calc(num1,num2,op='+'):
    if op=='-':
        result = sub(num1,num2)
    elif op=='*':
        result = mul(num1,num2)
    elif op=='/':
        result = div(num1, num2)
    else:
        result = sum(num1, num2)
    return(result)

# Example: Dividing 1 by 5
print(calc(1,5,'/'))


