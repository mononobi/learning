# -*- coding: utf-8 -*-
"""
1. isinstance
2. datetime, date, time
3. exception handling
4. string formatting, join
"""

# isinstance is used to determine an object is of a certain type.
number = 1.2

print(type(number))

print(type(number) == int)

print(isinstance(number, (int, float)))
print(isinstance(number, int))

# datetime

from datetime import datetime, date, time, timedelta

my_datetime = datetime(2020, month=12, day=11, hour=23)
print(my_datetime)

print(my_datetime.date())
print(my_datetime.time())
print(my_datetime.hour)
print(datetime.now())
print(datetime.utcnow())
print(my_datetime.weekday())
print(datetime.now().weekday())

now = datetime.now()

diff = now - my_datetime
print(diff)
print(type(diff))

delta = timedelta(milliseconds=1300)
print(delta)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())

print(my_datetime >= now)

# gets the difference between datetime object and epoch date (somewhere in 1970s) in floating seconds.
print(now.timestamp())


my_datetime = datetime(2020, month=12, day=11, hour=23, minute=2, second=25 ) + timedelta(minutes=3, milliseconds=854, microseconds=25)
print(my_datetime)

# date

my_date = date(year=2009, month=2, day=23)
print(my_date)

print(my_date.today())


# time

my_time = time(hour=20, minute=3)
print(my_time)

# string formatting


message = 'Hello dear {name}, please input your age and {work}:'
message1 = message.format(name='Sheida', work='Job')
values = dict(name='Tarek', work='Musician')
message2 = message.format(**values)
print(message1)
print(message2)

# string join

a = [1, 2, 3, 4]
result = ':   '.join([str(item) for item in a])
result2 = ':'.join([])
print(result)
print(result2)

# list comprehensions

b = (1, 2, 3, 4)

results = {str(item) for item in a if item > 2}
print(results)


# exception handling

items = [1, 2, 3, 'a', 5, 'b']
new_items = []

try:
    for item in items:
        new_items.append(item.upper())
except (AttributeError, ImportError) as error:
    print(error)
    # raise error
except LookupError:
    raise Exception('I have errors.')

print(new_items)


try:
    pass
except (AttributeError, ImportError) as name:
    pass

except LookupError:
    pass
