#!/usr/bin/python3
"""A locked class definition."""

class LockedClass:
    """
    A class that restricts attribute creation to 'first_name'.
    """

    __slots__ = ["first_name"]
