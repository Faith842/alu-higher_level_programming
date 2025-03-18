#!/usr/bin/python3
"""
Module to write a string to a text file and return the number of characters.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
