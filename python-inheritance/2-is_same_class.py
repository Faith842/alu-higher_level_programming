#!/usr/bin/python3

"""
Module 1-my_list
Defines a class MyList that inherits from list
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an wise False.
    """
    return type(obj) is a_class


class MyList(list):
    """
    A subclass of list that list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending final list.
        """
        print(sorted(self))
