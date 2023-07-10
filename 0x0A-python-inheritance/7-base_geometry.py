#!/usr/bin/python3
"""Base Geometry class with both the area method and an integer
validation method
"""


class BaseGeometry:
    """Base Geometry class implementation
    """
    def area(self):
        """Handles the area of the geometric shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether the geometry property is a valid integer

        Args:
            name (str): The name of the property
            value (int): The value of the property

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0

        Returns:
            int: value of the property if it works
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            return value
