from datetime import date


def assert_positive_number(num):
    if not isinstance(num, (int, float)):
        raise Exception('Please input a number.')
    if num <= 0:
        raise Exception('Please input a positive number.')


def assert_valid_year(year):
    assert_positive_number(year)
    this_year = date.today().year
    if not (year>=1900 and year<=this_year):
        raise Exception('Year should be between 1900 and '+ str(this_year))


def is_list(lst):
    if not isinstance(lst, list):
        raise Exception('Please introduce a list')



