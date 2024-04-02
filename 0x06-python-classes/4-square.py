#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int): The size of a side of the square.
        """

        self.size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.size ** 2

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of a side of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
