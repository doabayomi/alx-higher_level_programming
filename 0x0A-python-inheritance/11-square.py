#!/usr/bin/python3
"""A Square implementation with the addition of a
string method to handle print and str
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class implementation
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): The length of a side of the square
        """
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns area of the square

        Returns:
            int : Area of the rectangle
        """
        return (self.__size * self.__size)

    def __str__(self):
        """Handle the print and str call on the square

        Returns:
            str: Object in the format [Square] <width>/<height>
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
