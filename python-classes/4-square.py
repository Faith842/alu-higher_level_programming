#!/usr/bin/python3
"""
Module for Square class definition.
"""


class Square:
    """
    A class that defines a square with size validation and area calculation.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size  # Using the setter to validate size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
