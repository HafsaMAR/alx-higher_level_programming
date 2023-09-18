#!/usr/bin/python3
"""Defines the class Base"""
import csv
import turtle
import os.path
import json


class Base:
    """Class that defines a base properties and functionality.

    Attributes:
        id (int): The identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the new instance of the Base class.

        Args:
            id (int, optional): Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string representation.

    Args:
        list_dictionaries (list): The list of dictionaries to be converted.

    Returns:
        str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to file.

        Args:
            list_objs (list): list of instances inherits of Base. for  example:
            list of Rectangle or Square instances.
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): _description_

        Returns:
            list: JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):

        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): double pointer to a dictionary.
            cls (any): class.

        To use the update method to assign all attributes, you must,
        create a “dummy” instance before:
        Create a Rectangle or Square instance with “dummy” mandatory,
        attributes (width, height, size, etc.),
        Call update instance method to this “dummy” instance to apply your,
        real values.
        You must use the method def update(self, *args, **kwargs).
        **dictionary must be used as **kwargs of the method update.
        You are not allowed to use eval.

        Returns:
            list: an instance with all attributes already set.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        # print("cls type --> {}".format(type(cls)))
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances - the type of these instances,
        depends on cls (current class using this method).
        You must use the from_json_string and create methods (implemented,
        previously).
        Args:
            cls (any): class.

        Returns:
            list: list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
            list_objs (list): objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): class.
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

        window.exitonclick()