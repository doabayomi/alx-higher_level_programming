#!/usr/bin/python3
"""A Rectangle Class implementation with the initialization,
area method overwriting the BaseGeometry implementation and
a method to handle the print call for the object
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle implementation of geometry
    """
    def __init__(self, width, height):
        """Initializes a Rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Returns the area of the rectangle instance

        Returns:
            int: Area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Handle the print and str call on the rectangle

        Returns:
            str: Object in the format [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
