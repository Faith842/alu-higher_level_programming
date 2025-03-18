#!/usr/bin/python3


"""
Module for saving an object to a file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    Args:
        my_obj (any): The object to be serialized.
        filename (str): The name of the file to save the JSON string.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
