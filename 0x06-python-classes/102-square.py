#!/usr/bin/python3
"""Defines square"""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (float or int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size to be set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is less than the other in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to the other in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than the other in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to the other in area."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
