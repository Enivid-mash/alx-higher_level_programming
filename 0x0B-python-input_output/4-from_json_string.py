#!/usr/bin/python3

"""
Defines a function to convert a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        json_str (str): The JSON string to be converted.

    Returns:
        obj: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
