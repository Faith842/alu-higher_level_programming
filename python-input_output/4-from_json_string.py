#!/usr/bin/python3


"""
This module contains a function to return the Python object representation
from a JSON string.

The function `from_json_string(my_str)` uses the `json.loads()` method to
deserialize a JSON string into a Python object.

Author: Denyse Ishimirwe
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object (data structure) represented by a JSON string.
    Args:
        my_str: A JSON string to be converted into a Python object.
    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    # Test cases
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14},
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_invalid_dict = """
        {"is_active": true, 12}
        """
        my_dict = from_json_string(s_invalid_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
