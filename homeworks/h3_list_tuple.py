# -*- coding: utf-8 -*-
"""
1. we have a list of numbers (float or integer) named 'numbers_list'.
   define a function to process each number and separate even and
   odd numbers into two separate lists (excluding float and negative numbers).

2. define a function to make the equivalent tuple of odd and even
   numbers lists from the first exercise. (search the web for help if needed)

3. define a function to loop through the 'numbers_list' while reaching to a negative number.
   then return the index of the negative number and the negative number itself and also
   remove that number from the list.

4. define a function to calculate the sum of numbers in each of even and odd numbers list.
   (do not use loop for this, search the web if needed)

5. define a function to return the maximum and minimum number in 'numbers_list'.

6. define a function to return a new single list from odd and even numbers lists.

Happy Coding!
"""

numbers_list = [56, 8.5, 4, 33, 90, 1003, 100.2, 10.0, 34,
                707, 606, 505, -19, 23, 44, 90, 67.6, -3.4]

"""
1. we have a list of numbers (float or integer) named 'numbers_list'.
   define a function to process each number and separate even and
   odd numbers into two separate lists (excluding float and negative numbers).
"""

even_list = []
odd_list = []


def find_evens_looped(num_list):
    for num in num_list:
    # for index, num in enumerate(num_list):
        """check if it is integer"""
        if round(abs(num)) == num:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
    even_list.sort()
    odd_list.sort()
    # return 'List of the even numbers', even_list, 'List of the odd numbers', odd_list
    return even_list, odd_list


print(find_evens_looped(numbers_list))


"""
2. define a function to make the equivalent tuple of odd and even
   numbers lists from the first exercise. (search the web for help if needed)
"""


def convert_to_tuple(num_list):
    even, odd = find_evens_looped(num_list)
    return tuple(even), tuple(odd)


"""
3. define a function to loop through the 'numbers_list' while reaching to a negative number.
   then return the index of the negative number and the negative number itself and also
   remove that number from the list.
"""


def remove_first_negative(num_list):
    i = n = None
    for index, num in enumerate(num_list):
        """check for non negative integers"""
        i = index
        n = num
        if num < 0:
            break
    num_list.remove(n)
    # return 'index, value', i, n, 'is removed: ', num_list
    return i, n, num_list


print(remove_first_negative(numbers_list))


"""
4. define a function to calculate the sum of numbers in each of even and odd numbers list.
   (do not use loop for this, search the web if needed)
   """


numbers_list = [56, 8.5, 4, 33, 90, 1003, 100.2, 10.0, 34,
                707, 606, 505, -19, 23, 44, 90, 67.6, -3.4]


def even_odds(num_list):
    # even_list = [num for num in num_list if num % 2 == 0 and abs(round(num)) == num]
    # odd_list = [num for num in num_list if num % 2 != 0 and abs(round(num)) == num]
    # unpacking function result into two separate items.
    eve, odd = find_evens_looped(num_list)
    evens = sum(eve)
    odds = sum(odd)
    return 'Sum of the even numbers =', evens, 'Sum of the odd numbers =', odds


print(even_odds(numbers_list))


"""
5. define a function to return the maximum and minimum number in 'numbers_list'.
"""


def mini_maxi(num_list):
    mini = min(num_list)
    maxi = max(num_list)
    return mini, maxi


print(mini_maxi(numbers_list))

"""
6. define a function to return a new single list from odd and even numbers lists.
"""


def new_list(num_list):
    # eve = [num for num in num_list if num % 2 == 0 and abs(round(num)) == num]
    # odd = [num for num in num_list if num % 2 != 0 and abs(round(num)) == num]
    # unpacking function result into two separate items.
    eve, odd = find_evens_looped(num_list)
    eve.extend(odd)
    eve.sort()
    return eve


print(new_list(numbers_list))
