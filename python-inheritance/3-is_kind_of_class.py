#!/usr/bin/python3

"""
Module 1-my_list
Defines a class MyList that inherits from list
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly otherwise False.
    """
    return type(obj) is a_class


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of.
    """
    return isinstance(obj, a_class)


class MyList(list):
    """
    A subclass of list that list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in original list.
        """
        print(sorted(self))
