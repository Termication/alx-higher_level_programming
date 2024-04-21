"""Contains the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class for representing squares.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The identifier of the square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value
