#!/usr/bin/python3

"""
Defines a function to convert a Python class
object to a JSON dictionary representation.
"""


def class_to_json(obj):
    """
    Convert a Python class object to a JSON dictionary representation.

    Args:
        obj: The object to be converted.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
