#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        """if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")"""
        self._validate_integer_positive(value, "width")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        """if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")"""
        self._validate_integer_positive(value, "height")
        self._height = value

    def _validate_integer_positive(self, value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __str__(self):
        return f"{{'_Rectangle__width': {self._width}, '_Rectangle__height': {self._height}}}"
