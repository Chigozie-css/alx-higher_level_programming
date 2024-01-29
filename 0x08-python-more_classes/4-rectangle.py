#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height).strip()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    if __name__ == "__main__":
        Rectangle = __import__('4-rectangle').Rectangle

        my_rectangle = Rectangle(2, 4)
        print(str(my_rectangle))
        print("--")
        print(my_rectangle)
        print("--")
        print(repr(my_rectangle))
        print("--")
        print(hex(id(my_rectangle)))
        print("--")

    # create a new instance based on representation
        new_rectangle = eval(repr(my_rectangle))
        print(str(new_rectangle))
        print("--")
        print(new_rectangle)
        print("--")
        print(repr(new_rectangle))
        print("--")
        print(hex(id(new_rectangle)))
        print("--")

        print(new_rectangle is my_rectangle)
        print(type(new_rectangle) is type(my_rectangle))
