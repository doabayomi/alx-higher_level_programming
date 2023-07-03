#!/usr/bin/python3
"""Rectangle class definition

A rectangle defined by the width and height
made with the getters and setters and an initialization
There is also an area, perimeter function handled in it. There is a handling
function for the print() and str() call case. There is also a handling for the
repr function.

The deletion instance is being handled
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
            else:
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
            else:
                self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Finds the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle's representation
        """
        if self.__width == 0 or self.__height == 0:
            print("", end="")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __repr__(self):
        """Returns a string representation of the Rectangle

        Returns:
            str: The string representation of the Rectangle
        """
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the Rectangle class instance
        """
        print("Bye rectangle...")
