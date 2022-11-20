# -*- coding: utf-8 -*-
"""
1. file generation, modification
"""

# write and overwrite:
with open('/home/mono/workspace/learning/files/text.txt', mode='w') as file:
    file.write('line1\r\n')
    file.writelines(['line2\r\n', 'line3\r\n'])


# write and append:
with open('/home/mono/workspace/learning/files/append.txt', mode='a') as file:
    file.write('line1\r\n')
    file.writelines(['line2\r\n', 'line3\r\n'])

# Q: what can \r do for us? cursor at beginning. but how?

# read whole file:
with open('/home/mono/workspace/learning/files/append.txt', mode='r') as file:
    result = file.read()


# read lines:
with open('/home/mono/workspace/learning/files/append.txt', mode='r') as file:
    result2 = file.readline()
