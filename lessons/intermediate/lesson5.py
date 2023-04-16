# -*- coding: utf-8 -*-
"""
1. decorators.
"""
import time

from functools import update_wrapper
from time import sleep


class City:

    @property
    def size(self):
        return 0


def audit(func):
    """
    decorator to log execution time of a function.

    :param function func: function.

    :returns: function result.
    """

    def decorator(*args, **kwargs):
        """
        decorates the given function and logs its execution time.

        note that `audit_log: true` is required in logging config
        store for each environment to enable this decorator.

        :param object args: function arguments.
        :param object kwargs: function keyword arguments.

        :returns: function result.
        """

        start_time = time.time()
        try:
            return func(*args, **kwargs)

        finally:
            end_time = time.time()
            print('Duration of function call [{name}]: [{time} ms].'
                  .format(name=str(func),
                          time='{:0.5f}'
                          .format((end_time - start_time) * 1000)))

    return update_wrapper(decorator, func)


@audit
def test(a):
    """
    aaa
    :param a:
    :return:
    """
    sleep(a)
    print('Done')


test(3)
