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
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object

        Args:
            size (int): The size of the square
        """
        tuple_msg = "position must be a tuple of 2 positive integers"
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        else:
            raise TypeError("size must be an integer")

        if (not isinstance(position, tuple)) or (len(position) != 2):
            raise TypeError(tuple_msg)
        else:
            for i in position:
                if not isinstance(i, int):
                    raise TypeError(tuple_msg)
            self.__position = position

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

    @property
    def position(self):
        """Returns the position of the square

        Returns:
            tuple: The position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value (tuple): the new position of the square
        """
        msg = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple)) or (len(value) != 2):
            raise TypeError(msg)
        else:
            for i in value:
                if not isinstance(i, int):
                    raise TypeError(msg)
            self.__position = value

    def area(self):
        """Finds the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the elements of the print function
        """
        if self.__position[1] > 0:
            space = "_"
        else:
            space = " "

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for o in range(self.__position[0]):
                    print(space, end="")

                for j in range(self.__size):
                    print("#", end="")
                print()
