#!/usr/bin/python3

"""
This module defines the Square class that Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a from Rectangle."""

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Returns the official string representation.
        """
        return f"[Square] {self.__size}/{self.__size}"
