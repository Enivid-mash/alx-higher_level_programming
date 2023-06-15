#!/usr/bin/python3

"""
Defines a function to read a JSON file and create
a Python object from its contents.
"""

import json


def load_from_json_file(filename):
    """
    Read a JSON file and create a Python object from its contents.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        obj: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
