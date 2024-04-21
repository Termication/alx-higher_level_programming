"""Contains the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class for representing rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The identifier of the rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
            rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            rectangle's position. Defaults to 0.
            id (int, optional): The identifier of the
            rectangle instance. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
