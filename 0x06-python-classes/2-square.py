#!/usr/bin/python3
"""An implementation of the Square class

This implementation has the size attribute made private
to protect its type with type restriction and error raising
"""


class Square:
    """A class that defines a square

    Attributes:
       size (int): The size of the square
    """
    def __init__(self, size=0):
        """Initializes a square object

        Args:
            size (int): The size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        else:
            raise TypeError("size must be an integer")
