#!/usr/bin/python3
"""
Module for reading and printing a file's content.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str):The name of the file to read.Default is an empty string
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
