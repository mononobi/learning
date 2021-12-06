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


# dt = [d for d in mixed if isinstance(d, (datetime, date, time, timedelta))] # that is the correct way to compare Type, NOT with type castig: type() !!
# num = [n for n in mixed if type(n) in (int, float)]


# TODO: Your code goes here:
#from datetime import datetime, date, time, timedelta

def sorting_out():
    #result = []
    for item in objects:
        if isinstance(item, (datetime, date, time, timedelta)):
            date_times.append(item)
        elif isinstance(item, (int, float)) and not isinstance(item, bool): # beacuase bool is a sub type from int
            numbers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (list, set, tuple)):
            sequences.append(item)
        elif isinstance(item, dict):
            dictionaries.append(item)
        else:
            unknown.append(item)


sorting_out()


"""
2. write a function to return a message showing the count of items in 
   each one of the above lists. for example: numbers = 3, strings = 2, ...
"""

# TODO: Your code goes here:


def length():
    num_num = len(numbers)
    num_str = len(strings)
    num_dt = len(date_times)
    num_dic = len(dictionaries)
    num_seq = len(sequences)
    num_na = len(unknown)

    message = "Number of items:\n  Numbers:{num_num}\n  Strings:{num_str}\n  Date&Time:{num_dt}\n" \
              "  Dictionaries:{num_dic}\n  Sequences:{num_seq}\n  Unknown:{num_na}"
    message = message.format(num_num=num_num, num_str=num_str, num_dt=num_dt, num_dic=num_dic, num_seq=num_seq, num_na=num_na)
    print(message)

# call
length()

"""
3. write a function to return a message showing the items of date_times list separated 
   by double dashes `--`.
"""


# TODO: Your code goes here:
# keyword: join

def message_list(alist):
    message = '--'.join([str(n) for n in alist])
    return message

print(message_list(date_times))

"""
4. write a function to get the datetime of tomorrow from now.
"""

# TODO: Your code goes here:
# keyword: check the methods of Datetime and Timedelta (choose, ctrl, click)
def tomorrowi():
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    return tomorrow


print(tomorrowi())

"""
5. write a function which takes a single date object and returns the date of 7 days ago.
"""

# TODO: Your code goes here:
def week_ago(dt):
    #now = date.now()
    last_week = dt + timedelta(days=-7)
    return last_week

print(week_ago(date.today()))

"""
6. write a function which takes two datetime objects and returns the difference 
   between them as positive seconds.
"""

# TODO: Your code goes here:
def dt_dif(dt1, dt2):
    dif = dt1 - dt2
    dif_sec = dif.total_seconds()
    return abs(int(dif_sec))


print(dt_dif(datetime.now(), datetime(2020, 2, 11)))

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
def bigger_times():
    lt = []
    for t in datetime_items:
        if t.time() > single_time:
            lt.append(t)
    return lt


print(bigger_times())


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
def check_my_list():
    for i in numbers_list:
        try:
            output = validate_number(i)
            print(output)
        except (NegativeNumberError, InvalidNumberError) as err:
            print(err)
            continue
        except NoneNumberError:
            continue


check_my_list()

