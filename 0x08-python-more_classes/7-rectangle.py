#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        type(self).number_of_instances += 1
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
            return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            if isinstance(self.print_symbol, list):
                [rect.append(str(s)) for s in self.print_symbol]
            else:
                [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    if __name__ == "__main__":
        my_rectangle_1 = Rectangle(8, 4)
        print(my_rectangle_1)
        print("--")
        my_rectangle_1.print_symbol = "&"
        print(my_rectangle_1)
        print("--")

        my_rectangle_2 = Rectangle(2, 1)
        print(my_rectangle_2)
        print("--")
        Rectangle.print_symbol = "C"
        print(my_rectangle_2)
        print("--")

        my_rectangle_3 = Rectangle(7, 3)
        print(my_rectangle_3)

        print("--")

        my_rectangle_3.print_symbol = ["C", "is", "fun!"]
        print(my_rectangle_3)

        print("--")
