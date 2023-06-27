#!/usr/bin/python3
"""An implementation of the Square class

This implementation has the size attribute made private
to protect its type
"""


class Square:
    """A class that defines a square

    Attributes:
       size (int): The size of the square
    """
    def __init__(self, size):
        """Initializes a square object

        Args:
            size (int): The size of the square
        """
        self.__size = size
