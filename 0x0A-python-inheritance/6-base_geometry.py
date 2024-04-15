#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """Represents a base geometry class with a public attribute 'area'."""
    def area(self):
        """Raises an exception when called."""
        raise Exception("area() is not implemented")
