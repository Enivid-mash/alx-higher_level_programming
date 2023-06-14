#!/usr/bin/python3
"""
A script containing function that appends a string at the
end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append the specified text to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a") as file:
        return file.write(text)
