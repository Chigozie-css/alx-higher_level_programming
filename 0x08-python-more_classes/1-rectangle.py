#!/usr/bin/python3

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self._validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self._validate_dimension(value, "height")
        self.__height = value

    def _validate_dimension(self, value, name):
        """Validate the dimension (width or height)."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"{{'_Rectangle__height': {self.__height}, '_Rectangle__width': {self.__width}}}"
