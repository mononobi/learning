def assert_positive_number(num):
    if not isinstance(num, (int, float)):
        raise Exception('Please input a number.')
    if num <= 0:
        raise Exception('Please input a positive number.')
