# models/base.py

class Base:
    """
    Base class for managing id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique id.

        Args:
            id (int): The identifier for the instance. If None, assigns a new id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
