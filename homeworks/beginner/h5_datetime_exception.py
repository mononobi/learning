# -*- coding: utf-8 -*-
"""
1. we have a list with different objects in it, named objects.
   we also have 6 more empty lists, named: date_times, numbers,
   strings, sequences, dictionaries, unknown.
   write a function to to loop through the objects list and put each item in
   its relevant list.
   for clarification:
   datetime, date, time, timedelta -----> datetime_list
   int, float                      -----> numbers
   str                             -----> strings
   list, set, tuple                -----> sequences
   dict                            -----> dictionaries
   other objects                   -----> unknown
"""

from datetime import datetime, date, time, timedelta


objects = ['name', 10.4, True, 98, -9, 'Tree', [], datetime.now(),
           None, (1, 3, 4), {'a', 'b', 3}, date.today(), False, 0, bool,
           time(hour=13, second=10), int, [tuple, set], 'age', dict(),
           datetime.now, dict(name='Joe', age=39), dict, type(5), -4.6,
           bytes([1, 3]), timedelta(hours=10), {None}]

date_times = []
numbers = []
strings = []
sequences = []
dictionaries = []
unknown = []

# TODO: Your code goes here:


"""
2. write a function to return a message showing the count of items in 
   each one of the above lists. for example: numbers = 3, strings = 2, ...
"""

# TODO: Your code goes here:


"""
3. write a function to return a message showing the items of date_times list separated 
   by double dashes `--`.
"""

# TODO: Your code goes here:


"""
4. write a function to get the datetime of tomorrow from now.
"""

# TODO: Your code goes here:


"""
5. write a function which takes a single date object and returns the date of 7 days ago.
"""

# TODO: Your code goes here:


"""
6. write a function which takes two datetime objects and returns the difference 
   between them as positive seconds.
"""

# TODO: Your code goes here:


"""
7. we have a time object and a list of datetime objects.
   write a function which loops through the list of datetime objects and
   returns a new list of those values which their time part is greater than
   the time object.
"""

single_time = time(hour=14, minute=23, second=40)

datetime_items = [datetime.now(),
                  datetime(year=2020, month=1, day=3, hour=14, minute=23, second=40),
                  datetime(year=2000, month=10, day=23, hour=15),
                  datetime(year=2017, month=4, day=23, hour=14, minute=22, second=40),
                  datetime(year=1990, month=8, day=14, hour=16, minute=1, second=1)]

# TODO: Your code goes here:


"""
8. we have a function which takes a number as input named 'validate_number'.
   it returns the same number if it is between 1 and 100.
   it raises an exception if the number is negative.
   and it raises another type of exception on all other situations.
   write a function which takes a single input as list of numbers and prints
   the result of the above method for each number in the list or prints the error 
   message for each number. 
   there's a single condition, if the raised exception is 'NoneNumberError',
   it should not print anything for that number and must continue with the next number.
   
   you could use the sample list below as input to your function.
"""

numbers_list = [1, 40, 101, -9, 0, None, 80, 190, -100, None, 100]


class NegativeNumberError(Exception):
    pass


class InvalidNumberError(Exception):
    pass


class NoneNumberError(Exception):
    pass


def validate_number(value):

    if value is None:
        raise NoneNumberError('Number could not be None.')

    elif 1 <= value <= 100:
        return value

    elif value < 0:
        raise NegativeNumberError('Negative numbers are not allowed.')

    else:
        raise InvalidNumberError('Number [{number}] is not valid.'.format(number=value))


# TODO: Your code goes here:
