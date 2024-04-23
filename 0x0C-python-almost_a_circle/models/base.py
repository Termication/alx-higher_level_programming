#!/usr/bin/python3
# models/base.py
import csv
import json
import os
import turtle

class Base:
    """
    Base class for managing id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique id.

        Args:
            id (int): The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON representation of a list of dictionary
        Raises:
        TypeError: If list_dictionaries is not a list of dictionaries.

        Returns:
        str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a JSON representation of a list of objects to a file.

        Args:
            cls (class): The class itself.
            list_objs (list): The list of objects to save to the file.

        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string representation into a list of dictionaries.
        Returns:
        list: A list of dictionaries representing the JSON data.
        """
        deserialized_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            deserialized_list = json.loads(json_string)

        return deserialized_list
