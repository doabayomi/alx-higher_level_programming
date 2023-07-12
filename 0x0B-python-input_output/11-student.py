#!/usr/bin/python3
"""Adds method to Student Class to represent in json."""


class Student:
    """Implementation of a student."""

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve Dictionary Representation of object.

        Args:
            attrs (list, optional): List of attributes to retrieve.

        Returns:
            dict: Dictionary representaton of object
        """
        rep = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        if attrs is not None:
            return {attr: rep[attr] for attr in attrs if attr in rep}
        else:
            return rep

    def reload_from_json(self, json):
        """Replace all attributes of the student instance.

        Args:
            json (dict): Dictionary with new attributes to update to
        """
        for key, value in json.items():
            self.__setattr__(key, value)
