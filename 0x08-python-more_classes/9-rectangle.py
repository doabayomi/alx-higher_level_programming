#!/usr/bin/python3
"""Rectangle class definition

A rectangle defined by the width and height made with the getters and setters.
It has a value keeping track of the number of instances of the class.
There is also an area, perimeter function handled in it. There is a handling
function for the print() and str() call case. There is also a handling for the
repr function.

The deletion instance is being handled. There is a comparison function and a
method to make a square
"""


class Rectangle:
    """A rectangle class instance

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        number_of_instances (int): The number of current instances
        print_symbol: The print symbol for the __str__ method
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle Instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += str(self.print_symbol)
                string += '\n'
            return string

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
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area

        Args:
            rect_1 (Rectangle): The first rectangle instance
            rect_2 (Rectangle): The second rectangle instance

        Returns:
            Rectangle: rect_1 if it is bigger or equal, rect_2 otherwise
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a rectangle instance with equal width and height

        Args:
            cls: The class object
            size: The size of the square

        Returns:
            Rectangle: The square instance
        """
        sqr = cls()
        sqr.width = size
        sqr.height = size
        return sqr
