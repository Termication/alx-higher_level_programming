#!/usr/bin/python3
"""
Defines the BaseGeometry class and its subclasses Rectangle and Square.
"""


class BaseGeometry:
    """Defines geometric operations."""
    def area(self):
        """Raises an exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Instantiates the rectangle with specified width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns an informal string representation of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


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

    def __str__(self):
        """Returns an informal string representation of the square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
