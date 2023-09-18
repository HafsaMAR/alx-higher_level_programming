#!/usr/bin/python3

"""Module for the class Base"""


import json
import csv

class Base:
    """Base class
        Attributes:
        id (int): The identity of each instance.
        """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the id attribute of Base
        
        Args:
            id: optional variable
        """
        
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON representation of lists of dictionaries
        
        ARGS:
            list_dictionaries ([{}]): lsit of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        try:
            with open(cls.__name__ + '.json', 'w') as file:
                file.write(cls.to_json_string(list_dicts))
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error while saving to file: {e}")

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of a class and set its attributes
        based on a dictionary of values
        
        Args:
            dictionary: variable number of keyworded parameters
        
        Returns : instance of the class with its attributes set
        """
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Function that loads dictionaries from json file and
        return list of dictionaries stores
        
        Args:
            cls(Rectangle/Square): class
            
        Returns:
            list of dictionaries
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.read()
                json_dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in json_dictionaries]
                return instances
        except (FileNotFoundError, PermissionError) as e:
            return []
    # @classmethod
    # def save_to_file_csv(cls, list_objs):
    #     """save into a csv file
        
    #     Args:
    #         list_objs: object list
    #     """
    #     with open(cls.__name__ + ".csv", "w") as fcsv:
    #         if cls.__name__ == "Rectangle":
    #             writer = csv.writer(fcsv)
    #             for item in list_objs:
    #                 writer.writerow()