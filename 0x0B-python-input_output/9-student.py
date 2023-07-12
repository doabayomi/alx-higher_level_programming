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

    def to_json(self):
        """Retrieve dictionary representation of a student.

        Returns:
            dict: Dictionary representation of student
        """
        representation = {}
        representation["first_name"] = self.first_name
        representation["last_name"] = self.last_name
        representation["age"] = self.age
        return representation
