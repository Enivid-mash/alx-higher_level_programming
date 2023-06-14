#!/usr/bin/python3

"""
Defines a function to convert a Python object to a JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string representation.

    Args:
        obj: The object to be converted.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
