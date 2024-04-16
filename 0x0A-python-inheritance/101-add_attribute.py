#!/usr/bin/python3
"""Module for adding attributes to objects."""


def add_attribute(prmObject, prmName, prmValue):
    """Adds an attribute to an object."""
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("Can't add new attribute.")
    if not hasattr(prmObject, prmName):
        prmObject.__setattr__(prmName, prmValue)
