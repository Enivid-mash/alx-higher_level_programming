#!/usr/bin/python3
"""
This module contains a base class to serve as a
foundation for other classes.
"""


class Base:
    """
    Represents the base class for all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        If an id is provided, assigns it to the instance's id attribute.
        Otherwise, increments the __nb_objects counter and assigns its
        value to the instance's id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
