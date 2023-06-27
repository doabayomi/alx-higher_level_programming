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

    @property
    def size(self):
        """Returns the size of the square

        Returns:
            int: The size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of the square

        Args:
            value (int): the new size of the square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = int(value)
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Finds the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the elements of the print function
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
