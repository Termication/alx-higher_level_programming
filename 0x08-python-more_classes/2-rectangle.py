#!/usr/bin/python3
"""Implementation of a Rectangle class"""


class Rectangle:
    """Defines a rectangle object"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance with given width and height
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
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0
