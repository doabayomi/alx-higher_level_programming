#!/usr/bin/python3
"""Base Class Definition."""
import json
from os.path import exists


class Base:
    """Base Class Definition (Foundation for other classes)."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base class intance.

        Args:
            id (int, optional): Id of instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionary to JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            json: JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json representation of list_objs to file.

        Args:
            list_objs (list): list of instances
        """
        obj_list = []
        classname = cls.__name__
        if list_objs is not None:
            for instance in list_objs:
                obj_list.append(instance.to_dictionary())
                json_string = cls.to_json_string(obj_list)
        file_name = "{}.json".format(classname)
        with open(file_name, "w") as fp:
            fp.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return a list from a JSON string.

        Args:
            json_string (str): The JSON string

        Returns:
            list: The corresponding list of the JSON string
        """
        rep_list = []
        if json_string is None or len(json_string) == 0:
            return rep_list
        rep_list = json.loads(json_string)
        return rep_list

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance with set attributes.

        Returns:
            Rectangle / Square: The new instance
        """
        if cls.__name__ == "Rectangle":
            s = cls(2, 3)
        else:
            s = cls(2)
        s.update(**dictionary)
        return s

    @classmethod
    def load_from_file(cls):
        """Load instances from file.

        Returns:
            list: List of the instances in the file
        """
        file_name = "{}.json".format(cls.__name__)
        instance_list = []
        if not exists(file_name):
            return instance_list

        with open(file_name, "r") as fp:
            data = fp.read()
        data_list = cls.from_json_string(data)
        for instance in data_list:
            new_instance = cls.create(**instance)
            instance_list.append(new_instance)
        return instance_list
