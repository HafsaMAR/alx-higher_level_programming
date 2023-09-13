#!/usr/bin/python3

"""Module for Class Student with filter"""


class Student:
    """Class student with filter"""
    def __init__(self, first_name, last_name, age) -> None:
        """
        initialization of the attributes
        args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Methode that retrieves a dictionary
        representation of a Student instance

        Args:
            attrs: atributs of the student class

        returns:
            dictionary representation of the instance
        """
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dict[key] = value
            return (dict)

    def reload_from_json(self, json):
        """
        Replace all attributes to the student instance

        Args:
            json (dict): dictionary of new attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
