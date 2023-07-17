#!/usr/bin/python3
"""Square Class Implementation from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Implementation for a Square implementation.

    Args:
        Rectangle (class): The Rectangle Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

        Args:
            size (int): The size of the square
            x (int, optional): x offset of the square. Defaults to 0.
            y (int, optional): y offset of the square. Defaults to 0.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of a Square.

        Returns:
            str: The string representation of the square
        """
        x_y = "{}/{}".format(self.x, self.y)
        size_desc = "{}".format(self.width)
        sqr_desc = "[Square] ({})".format(self.id)
        final_string = sqr_desc + " " + x_y + " - " + size_desc
        return final_string

    @property
    def size(self):
        """Returns the size of the square.

        Returns:
            int: The size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of a square.

        Args:
            size (int): The size of a square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the values of the member of a square.

        Description:
            This function updates the values of all the members of the
            list in the order "id", "size", "x" and "y"

        Args:
            *args: The argument array
            *kwargs: Key value pair of the arguments
        """
        if len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Return a dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square
        """
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['size'] = self.size
        dict_rep['x'] = self.x
        dict_rep['y'] = self.y
        return dict_rep
