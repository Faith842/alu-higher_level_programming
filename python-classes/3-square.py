#!/usr/bin/python3


"""This module defines a class Square with a private size attribute.
It includes validation to ensure that size is an integer and is greater than or
equal to 0.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the square with a given size, which defaults to 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
