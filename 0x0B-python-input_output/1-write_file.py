#!/usr/bin/python3
"""
This script defines a function that writes text to a file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Function: write_file()
    Writes the given text to the specified file.
    """
    with open(filename, 'w') as file_object:
        return file_object.write(text)
