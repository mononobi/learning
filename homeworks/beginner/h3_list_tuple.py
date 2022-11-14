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

# 1st Assignment:

even_list = []
odd_list = []

for number in numbers_list:
    if number > 0 and isinstance(number, int):
        reminder = number % 2
        if reminder == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

print('1st assignment:')
print('even list: ', even_list)
print('odd list: ', odd_list)


# 2nd Assignment:

def list_to_tuple(list_of_numbers):
    """returns tuple evuivalent of a list"""
    return tuple(list_of_numbers)
print('\n2nd assignment has no results')


# 3rd Assignment:

print('\n3rd assignment:')
def negative_number_remover(list_of_numbers):
    """returns the negative value and its index from a list and then removes it."""
    for index, number in enumerate(list_of_numbers):
        if number < 0:
            print("negative index: ", index,"\tnegative number: ", number)
            list_of_numbers.remove(number)
    print('new list without negative numbers:', numbers_list)

negative_number_remover(numbers_list)

# 4th assignment:

def recursive_sum(list_sum, start=0):
    """returns the sum of elements of a list."""
    if not list_sum:
        return start
    else:
        return recursive_sum(list_sum[1:], start + list_sum[0])

print('\n4th assignment:')

print('sum of list: ', recursive_sum(odd_list, 0))


# 5th assignment:
def min_max_list(list_of_numbers):
    """returns min and max of given list."""
    return min(numbers_list), max(numbers_list)


print('\n5th assignment:')
print ('min and max of list: ', min_max_list(numbers_list))


# 6th assignment:

def cumulative_list(list1, list2):
    new_list = list1 + list2
    return new_list


print('\n6th assignment:')
print ('combined list: ', cumulative_list(odd_list, even_list))