#!/usr/bin/python3
"""
Square Module

This module contains a Square class that represents a geometric square.
The class provides functionality to manipulate squares, including setting
and getting the size of a square, calculating its area, and comparing squares.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of a side of the square.
        """
        self.size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of a side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of a side of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Comparison methods"""

    def __lt__(self, other):
        """Checks if the square is smaller
        than the other square by area."""
        return self.size < other.size

    def __le__(self, other):
        """Checks if the square is smaller or
        equal to the other square by area."""
        return self.size <= other.size

    def __eq__(self, other):
        """Checks if the square is equal to
        the other square by area."""
        return self.size == other.size

    def __ne__(self, other):
        """Checks if the square is not equal
        to the other square by area."""
        return self.size != other.size

    def __ge__(self, other):
        """Checks if the square is greater or
        equal to the other square by area."""
        return self.size >= other.size

    def __gt__(self, other):
        """Checks if the square is greater
        than the other square by area."""
        return self.size > other.size
