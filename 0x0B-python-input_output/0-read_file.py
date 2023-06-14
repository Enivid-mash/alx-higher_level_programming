#!/usr/bin/python3
"""
This script defines a function that reads a text file (UTF8)
and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Function: read_file()
    Prints the content of a file
    """
    with open(filename) as file_object:
        print(file_object.read(), end='')
