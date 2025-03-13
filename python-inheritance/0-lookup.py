#!/usr/bin/python3

"""Module providing the lookup methods of an object."""


def lookup(obj):
    """Returns a list of available attributes.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
