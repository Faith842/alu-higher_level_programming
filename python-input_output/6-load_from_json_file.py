#!/usr/bin/python3


"""
Module for creating an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the file to read the JSON string from.
    Returns:
        The object created from the JSON string.
    """
    with open(filename, 'r') as file:
        return json.load(file)
