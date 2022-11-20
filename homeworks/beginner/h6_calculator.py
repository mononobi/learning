# -*- coding: utf-8 -*-
"""
a simple calculator app.
"""

import h1_calculator

def show_help_get_inputs_show_result():
    """
    Using homework h1 we give the user the options to put two numbers and an operator to calculate on them.
    """

    try:
        print(h1_calculator.calculator_func.__doc__)

        number_one = int(input("Enter number one: "))
        number_two = int(input('Enter number two: '))
        operator = input('Which operator? (a, b, c, d) ')

        # Q: how can we specify int and float from input string? note: int on float generates error.

        result = h1_calculator.calculator_func(number_one, number_two, operator)
        print(result)

    except ZeroDivisionError:
        print('Division by zero is impossible.')

    except ValueError:
        print('Please enter a number.')

        # Q: I have another ValueError that I want to respond differently. if you put float, you get this error.



if __name__ == '__main__':
    repeat = True
    while repeat:
        show_help_get_inputs_show_result()
        repeat = bool(int(input('Enter anything to continue another calculation, Enter 0 (zero key) to exit: ')))

