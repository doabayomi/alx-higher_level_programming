#!/usr/bin/python3
"""Rectangle class definition
"""


class Rectangle:
    """A rectangle class instance

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        number_of_instances (int): The number of instances existing
        print_symbol: The character/element used to draw the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle Instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
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
            self.__width = value

    @property
    def height(self):
        """Gets the height Attribute

        Returns:
            int: The height of the rectangle instance
        """
        return self.__height

    @height.setter
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
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Finds the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle's representation
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string += str(self.print_symbol)
                if not (i == (self.height - 1)):
                    string += '\n'
            return string

    def __repr__(self):
        """Returns a string representation of the Rectangle

        Returns:
            str: The string representation of the Rectangle
        """
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """Deletes the Rectangle class instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
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
        sqr = cls(size, size)
        return sqr
