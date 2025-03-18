#!/usr/bin/python3
"""
Module to append a string to a text file and return the NO of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of
    characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
