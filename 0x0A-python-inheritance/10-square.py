#!/usr/bin/python3

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
