#!/usr/bin/python3

"""
This module defines the class BaseGeometry with.
"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception because area() is."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
