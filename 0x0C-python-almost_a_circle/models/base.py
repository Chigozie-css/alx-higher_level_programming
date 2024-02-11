#!/usr/bin/python3
"""Module defining the Base class."""

import json

class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by json_string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes set.

        Args:
            dictionary (dict): Dictionary containing attribute values.

        Returns:
            Base: Instance with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Invalid subclass")

        dummy_instance.update(**dictionary)  # Update dummy instance with dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a file.

        Returns:
            list: List of instances loaded from file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    # Example usage of Base class
    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
