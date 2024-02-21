import math

class MagicClass:
    """Represents a magic class."""

    def __init__(self, radius=0):
        """Initialize the magic class with a radius."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate the area of the magic class."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the magic class."""
        return 2 * math.pi * self._MagicClass__radius
