#!/usr/bin/python3

"""
- 'width' and 'height' must be integers.
- 'width' and 'height' must be greater than or equal to zero.
It also tracks the number of instances of the Rectangle class.
It prints a message when an instance is deleted.
"""


class Rectangle:
    """
    the values are integers and non-negative.
    Also tracks the number of instances of Rectangle.
    Prints a message when an instance is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Arguments:
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """
        using the eval() function.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when the rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
