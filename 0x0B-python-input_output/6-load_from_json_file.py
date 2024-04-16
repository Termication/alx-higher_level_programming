#!/usr/bin/python3

"""Defines a function for loading objects from JSON files."""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        obj: The Python object loaded from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
