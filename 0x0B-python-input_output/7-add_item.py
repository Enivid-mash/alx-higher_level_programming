#!/usr/bin/python3

"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
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


def save_to_json_file(obj, filename):
    """
    Write a Python object to a JSON file.

    Args:
        obj: The object to be written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as file:
        json.dump(obj, file)


def add_arguments_to_list(arguments):
    """
    Add the provided arguments to a Python list.

    Args:
        arguments (list): The arguments to be added to the list.

    Returns:
        list: The updated list with the added arguments.
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(arguments)
    return items


if __name__ == "__main__":
    arguments = sys.argv[1:]
    updated_list = add_arguments_to_list(arguments)
    save_to_json_file(updated_list, "add_item.json")
