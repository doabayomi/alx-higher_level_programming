#!/usr/bin/python3
"""Rectangle class definition

A rectangle defined by the width and height
made with the getters and setters and an initialization
"""


class Rectangle:
    """A rectangle class instance

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle Instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

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
        return self._height

    @width.setter
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
