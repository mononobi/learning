def assert_positive_number(num):
    if not isinstance(num, int) or num <= 0:
        raise Exception('Please input a positive number.')
