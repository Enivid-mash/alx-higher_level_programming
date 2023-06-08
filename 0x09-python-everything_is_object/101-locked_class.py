#!/usr/bin/python3
"""
Defines a locked class that restricts attribute creation.
"""


class LockedClass:
    """
    A class that restricts attribute creation to only 'first_name'.
    """

    __slots__ = ["first_name"]
