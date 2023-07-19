#!/usr/bin/python3
"""
This module contains a base class to serve as a
foundation for other classes.
"""

import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): The list of dictionaries.

        Returns:
            str: The JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): The list of instances.

        Returns:
            None.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary() for obj
                                         in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes set based on
        the provided dictionary.

        Args:
            **dictionary (dict): The dictionary of attribute values.

        Returns:
            Base: The created instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """
        Updates the attributes of an instance.

        Args:
            *args: The positional arguments.
            **kwargs: The keyword arguments.

        Returns:
            None.
        """
        if args:
            attrs = ["id", "width", "height", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                if json_data:
                    obj_list = cls.from_json_string(json_data)
                    instances = [cls.create(**obj_dict) for
                                 obj_dict in obj_list]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes instances to CSV format and saves to a file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]

                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                if file.readable():
                    reader = csv.DictReader(file)
                    instances = []
                    for row in reader:
                        obj_dict = {k: int(v) for k, v in row.items()}
                        instances.append(cls.create(**obj_dict))
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
