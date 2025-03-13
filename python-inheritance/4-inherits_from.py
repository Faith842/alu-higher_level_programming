#!/usr/bin/python3

"""
Module 1-my_list
Defines a class MyList that inherits from list
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is a_class, otherwise False.
    """
    return type(obj) is a_class


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an, a_class. Otherwise, returns False.
    """
    return isinstance(obj, a_class)


def inherits_from(obj, a_class):
    """
    Returns True if obj is an from a_class.
    Otherwise, returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


class MyList(list):
    """
    A subclass of list that includes sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order original list.
        """
        print(sorted(self))
