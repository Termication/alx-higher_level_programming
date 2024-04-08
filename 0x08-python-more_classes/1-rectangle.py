#!/usr/bin/python3
"""Defines a class representing a rectangle"""


class Rectangle:
    """Represents a rectangle shape"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with specified width and height
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
