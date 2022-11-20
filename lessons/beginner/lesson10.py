# -*- coding: utf-8 -*-
"""
1. finally block
2. running application from command line
3. input method
"""

# try, except, finally:

items = [1, 2, 3, -9, 10]

# in the first block on each error, the code execution will be continued.
for item in items:
    try:
        if item <= 0:
            raise Exception('Invalid Number.')
    except Exception as some_error:
        print(some_error)

    finally:
        print(item)


# in the second block, on first exception, the number will be
# printed but code execution will end immediately.

# UNCOMMENT TO SEE THE BEHAVIOR
# for item in items:
#     try:
#         if item <= 0:
#             raise Exception()
#
#     finally:
#         print(item)

# executing a python file using command line:

def multiply(num):
    return num * 2


def get_number():
    num = input('Please input a number: ')
    return int(num)


if __name__ == '__main__':
    num = get_number()
    print(multiply(num))


# COMMAND LINE ACTIONS:
# open cmd in windows.

# cd file_address: change working directory to "file_address"
# cd C:\windows

# dir: show list of all files and folders in current directory.

# python file_name.py: execute a python file.



# Q: how should I run file with a path on python terminal?

