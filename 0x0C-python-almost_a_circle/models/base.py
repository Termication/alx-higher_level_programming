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

    @classmethod
    def create(cls, **dictionary):
        """Creates and returns an instance with all attributes already set."""
        # Create an instance of the class
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file and returns a list of instances."""

        json_file_name = cls.__name__ + ".json"
        instances_list = []
        dictionaries_list = []

        if os.path.exists(json_file_name):
            with open(json_file_name, 'r') as file:
                json_str = file.read()
                dictionaries_list = cls.from_json_string(json_str)
                for dictionary in dictionaries_list:
                    instances_list.append(cls.create(**dictionary))
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves them to a CSV file."""
        csv_filename = cls.__name__ + ".csv"
        with open(csv_filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    csv_fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    csv_fieldnames = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csv_file,
                                            fieldnames=csv_fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes CSV format from a file and
        returns a list of instances.
        """
        csv_filename = cls.__name__ + ".csv"
        try:
            with open(csv_filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    csv_fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    csv_fieldnames = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(csvfile, fieldnames=csv_fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in csv_reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Utilizes the turtle module to visually
        represent Rectangles and Squares.

        Args:
            list_rectangles (list): A list of
            Rectangle objects to draw.
            list_squares (list): A list of
            Square objects to draw.
        """
        """Create a turtle object"""
        t = turtle.Turtle()
        """Set the background color of the drawing window"""
        t.screen.bgcolor("#b7312c")
        """Set the pen size"""
        t.pensize(3)
        """Set the shape of the turtle"""
        t.shape("turtle")

        """Draw rectangles"""
        t.color("#ffffff")  # Set color for rectangles
        for rect in list_rectangles:
            """Show the turtle"""
            t.showturtle()
            """Lift the pen up"""
            t.up()
            """Move turtle to the starting point of rectangle"""
            t.goto(rect.x, rect.y)
            """Put the pen down"""
            t.down()
            """Draw the rectangle"""
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            """Hide the turtle after drawing"""
            t.hideturtle()

        """Draw squares"""
        t.color("#b5e3d8")  # Set color for squares
        for sq in list_squares:
            """Show the turtle"""
            t.showturtle()
            """Lift the pen up"""
            t.up()
            """Move turtle to the starting point of square"""
            t.goto(sq.x, sq.y)
            """Put the pen down"""
            t.down()
            """Draw the square"""
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            """Hide the turtle after drawing"""
            t.hideturtle()

        """Allow user to click on the drawing window to close it"""
        turtle.exitonclick()
