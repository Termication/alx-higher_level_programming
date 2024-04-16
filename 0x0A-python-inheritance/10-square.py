#!/usr/bin/python3
"""
Defines the BaseGeometry class and its subclass Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        """Instantiates the square with the specified size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
