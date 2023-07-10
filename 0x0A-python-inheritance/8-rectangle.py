#!/usr/bin/python3

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
