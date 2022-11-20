# -*- coding: utf-8 -*-
"""
1. we have a list with different objects in it, named objects.
   we also have 6 more empty lists, named: date_times, numbers,
   strings, sequences, dictionaries, unknown.
   write a function to loop through the objects list and put each item in
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
import math

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

dict_of_lists = {'date_time': date_times,
                 'numbers': numbers,
                 'strings': strings,
                 'sequences': sequences,
                 'dictionaries': dictionaries,
                 'unknown': unknown}
class Animal:
    pass

class Sheep(Animal):
    pass


class WildSheep(Sheep):
    pass


sheep = Sheep()
print('HERE ', type(sheep) == Animal)
print('HERE ', isinstance(sheep, Animal))
print('HERE ', isinstance(sheep, Sheep))


def categorize_objects(objects1):
    """recieves a list of objects and categorize each type in a seperate list."""

    for item in objects1:
        if type(item) in (datetime, date, time, timedelta):
            dict_of_lists['date_time'].append(item)
        elif type(item) in (int, float, bool):
            dict_of_lists['numbers'].append(item)
        elif type(item) == str:
            dict_of_lists['strings'].append(item)
        elif type(item) in (list, set, tuple):
            dict_of_lists['sequences'].append(item)
        elif type(item) == dict:
            dict_of_lists['dictionaries'].append(item)
        else:
            dict_of_lists['unknown'].append(item)

    for key, value in dict_of_lists.items():
        print(f'{key}: {value}')

    return None


def categorize_objects_v2(objects1):
    """recieves a list of objects and categorize each type in a seperate list."""

    for item in objects1:
        if isinstance(item, (datetime, date, time, timedelta)):
            dict_of_lists['date_time'].append(item)
        elif isinstance(item, (int, float)) and not isinstance(item, bool):
            dict_of_lists['numbers'].append(item)
        elif isinstance(item, str):
            dict_of_lists['strings'].append(item)
        elif isinstance(item, (list, set, tuple)):
            dict_of_lists['sequences'].append(item)
        elif isinstance(item, dict):
            dict_of_lists['dictionaries'].append(item)
        else:
            dict_of_lists['unknown'].append(item)

    for key, value in dict_of_lists.items():
        print(f'{key}: {value}')

    return None


print('1st Assignment result:')
categorize_objects(objects)

"""
2. write a function to return a message showing the count of items in 
   each one of the above lists. for example: numbers = 3, strings = 2, ...
"""


# TODO: Your code goes here:

def count_items_lists(dict_of_lists1):
    """count the elements of each list in the dictionary of lists."""
    for key, value in dict_of_lists1.items():
        print(f'count of elements in {key} list is {len(value)}')


print('\n2nd Assignment result:')
count_items_lists(dict_of_lists)

"""
3. write a function to return a message showing the items of date_times list separated 
   by double dashes `--`.
"""


# TODO: Your code goes here:

def count_of_date_time(list1):
    """shows items of date_time list in a format"""

    content = '--'.join([str(item) for item in list1])
    print(content)

    return content


print('\n3rd Assignment result:')
count_of_date_time(date_times)

"""
4. write a function to get the datetime of tomorrow from now.
"""


# TODO: Your code goes here:

def show_datetime_of_tomorrow():
    """as name of function."""
    tomorrow_time = datetime.now() + timedelta(days=1)
    print(tomorrow_time)

    return tomorrow_time


print('\n4th Assignment result:')
show_datetime_of_tomorrow()

"""
5. write a function which takes a single date object and returns the date of 7 days ago.
"""


# TODO: Your code goes here:

def show_date_of_7_days_ago(date1):
    """receives a date object and shows date of 7 days ago."""
    seven_days_before_date = date1 + timedelta(days=-7)
    print(seven_days_before_date)

    return seven_days_before_date


print('\n5th Assignment result:')
date1 = date(year=2000, month=1, day=1)
show_date_of_7_days_ago(date1)

"""
6. write a function which takes two datetime objects and returns the difference 
   between them as positive seconds.
"""


# TODO: Your code goes here:

def show_diff_of_two_datetimes(datetime1, datetime2):
    """receives 2 dates and shows the difference."""
    datetime_diff = abs((datetime1 - datetime2).seconds)
    print(datetime_diff)

    return datetime_diff


print('\n6th Assignment result:')
datetime1 = datetime(year=2000, month=1, day=1)
datetime2 = datetime.now()
show_diff_of_two_datetimes(datetime1, datetime2)

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

def return_greater_times(time1, datetimes_1):
    """receives a time and a list of datetimes, and shows a list of greater time-part datetimes."""

    new_list = []
    for datetime_1 in datetimes_1:
        if datetime_1.time() > time1:
            new_list.append(datetime_1)
    print(new_list)

    return new_list


print('\n7th Assignment result:')
return_greater_times(single_time, datetime_items)

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

def validate_number_on_list(list1):
    """this function uses the validate_number function and ignores the NoneNumberError"""

    for item in list1:
        try:
            result = validate_number(item)
            print(result)

        except NoneNumberError:
            continue

        except Exception as error:
            print(error)


print('\n8th Assignment result:')
validate_number_on_list(numbers_list)


