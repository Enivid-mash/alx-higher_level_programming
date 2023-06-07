#!/usr/bin/python3

def magic_string():

    # Initialize magic_string.n if it doesn't exist, and increment it by 1
    magic_string.n = getattr(magic_string, 'n', 0) + 1

    # Create magic string
    return ("BestSchool, " * (magic_string.n - 1)) + "BestSchool"
