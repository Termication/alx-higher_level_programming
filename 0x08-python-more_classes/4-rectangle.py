#!/usr/bin/python3
"""Definition of Rectangle class"""


class Rectangle:
    """Represents a geometric rectangle shape"""

    def __init__(self, width=0, height=0):
        """Instantiate a rectangle with specified width and height
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        Raises:
            TypeError: If width or height are not integers
            ValueError: If width or height are less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Accessor method for retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Mutator method for setting the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Accessor method for retrieving the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Mutator method for setting the height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
