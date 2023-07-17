#!/usr/bin/python3
"""Rectangle class definition inherited from base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class Based on the Base Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle class based on the Base Class.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): x offset. Defaults to 0.
            y (int, optional): y offset. Defaults to 0.
            id (int, optional): Id of the instance. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of a rectangle.

        Args:
            width (int): New width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is <= 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of a rectangle.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of a rectangle.

        Args:
            height (int): The new height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is <= 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets the x offset of a rectangle.

        Returns:
            int: The x offset of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x offset of a rectangle.

        Args:
            x (int): The new x offset of the rectangle

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is <= 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the y offset of a rectangle.

        Returns:
            int: The y offset of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y offset of a rectangle.

        Args:
            y (int): The new y offset of the rectangle

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is <= 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Print the representation of the rectangle using the # symbol."""
        for i in range(self.y):
            print()

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return string representation of Rectangle Class.

        Returns:
            str: The string representation of the class
        """
        x_y = "{}/{}".format(self.x, self.y)
        width_height = "{}/{}".format(self.width, self.height)
        rect_desc = "[Rectangle] ({})".format(self.id)
        final_string = rect_desc + " " + x_y + " - " + width_height
        return final_string

    def update(self, *args, **kwargs):
        """Update the values of the member of a rectangle.

        Description:
            This function updates the values of all the members of the
            list in the order "id", "width", "height", "x" and "y"

        Args:
            *args: The argument array
            *kwargs: Key value pair of the arguments
        """
        if len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle
        """
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['width'] = self.width
        dict_rep['height'] = self.height
        dict_rep['x'] = self.x
        dict_rep['y'] = self.y
        return dict_rep
