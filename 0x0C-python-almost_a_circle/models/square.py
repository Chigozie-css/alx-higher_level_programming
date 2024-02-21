#!/usr/bin/python3
"""Module defining the Square class."""

from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance with size, x, y, and id.

        Args:
            size (int): The size of the square.
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Greater for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        #Return string representation of the square
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @staticmethod
    def save_to_file(list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of Square instances.
        """
        filename = "Square.json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(Base.to_json_string(json_list))

    @classmethod
    def load_from_file(cls):
        """
        Return a list of Square instances loaded from file.

        Returns:
            list: List of Square instances loaded from file.
        """
        filename = "Square.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = Base.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

if __name__ == "__main__":

    """Square Dictionary"""
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)


    """Updating the Square"""
    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(10, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)

    """Square size"""
    print(s1)
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
