#!/usr/bin/python3

"""Defines a function for saving objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
