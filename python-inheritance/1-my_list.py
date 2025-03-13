#!/usr/bin/python3

"""Module containing a sorting method."""


class MyList(list):
    """A subclass of list print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
