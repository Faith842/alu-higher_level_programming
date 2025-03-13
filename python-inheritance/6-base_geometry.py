#!/usr/bin/python3

"""
This module defines the class an exception.
"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raises an exception because implemented."""
        raise Exception("area() is not implemented")
