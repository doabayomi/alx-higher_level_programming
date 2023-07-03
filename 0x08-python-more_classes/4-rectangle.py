#!/usr/bin/python3
"""Rectangle class definition
"""


class Rectangle:
    """A rectangle class instance

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle Instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width Attribute

        Returns:
            int: The width of the rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute

        Args:
            value (int): The new value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """Gets the height Attribute

        Returns:
            int: The height of the rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute

        Args:
            value (int): The new value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Finds the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle's representation
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string = string + '#'
                if not (i == (self.height - 1)):
                    string += '\n'
            return string

    def __repr__(self):
        """Returns a string representation of the Rectangle

        Returns:
            str: The string representation of the Rectangle
        """
        return "Rectangle({0}, {1})".format(self.__width, self.__height)
