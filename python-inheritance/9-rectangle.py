#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits."""

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string description of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns the official string representation.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
