#!/usr/bin/python3

"""Module for the Class Square inheriting from Rectangle"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.rectangle import Rectangle

class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """
        Initialization of the class attribute
        
        Args:
            size (int): size of the square
            y (int): 
            x (int): 
        """
        self.__size = size
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """
            override the magic str methode
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes value using either keyworded or
        none-keyworded arguments
        
        ARGS:
            *args: non-keyworded variable length argument list
            **kwargs: keyworded variable length of arguments
        """
        Attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(Attributes):
                    setattr(self, Attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        
    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}