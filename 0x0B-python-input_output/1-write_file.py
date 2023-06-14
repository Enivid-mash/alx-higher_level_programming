#!/usr/bin/python3
"""
This script defines a function that reads a text file (UTF8)
and prints its contents to stdout.
"""


def write_file(filename="", text=""):
    """
    Function: read_file()
    Prints the content of a file
    """
    with open(filename, 'w') as file_object:
        return file_object.write(text)

