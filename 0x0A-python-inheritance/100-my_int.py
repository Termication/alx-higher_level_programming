#!/usr/bin/python3
"""
Defines the MyInt class.
"""


class MyInt(int):
    """
    Represents a rebellious version of an
    integer, perfect for opposite day!
    """
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Defines the opposite behavior for equality."""
        return int(self) != other

    def __ne__(self, other):
        """Defines the opposite behavior for inequality."""
        return int(self) == other
