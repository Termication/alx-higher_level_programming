#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): The size of a side of the square.
        Returns:
            None
        """

        self.size = size

    def area(self):
        """Calculates the square's area.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2

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
        Returns:
            None
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

    def my_print(self):
        """Prints the square.

        Returns:
            None
        """

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
