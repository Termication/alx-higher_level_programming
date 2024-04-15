#!/usr/bin/python3
"""
Defines the function is_same_class.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is of the exact
    class a_class, otherwise returns False."""
    return type(obj) == a_class
