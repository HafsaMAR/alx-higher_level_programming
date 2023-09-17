#!/usr/bin/python3

"""Module for the Rectangle class inheriting from Base class"""


from models.base import Base

class Rectangle(Base):
    """Class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
        initialization of the arguments
        
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of the rectangle
            y (int, optional): y coordinate of the rectangle
            id (int): optional parameter id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """get the value of the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Set the value of the rectangle width
        
        
        Args:
            value (int): new value for the width attribute
        
        Raise:
            TypeError: if width is not integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the value of height attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter of the height attribute
        
        Args:
            value (int): value of the height attribute
        
        Raise:
            TypeError if height is not integer
            ValueError if height is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value 
    
    @property
    def x(self):
        """getter of the x coordinate value"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        Setter of the x coordinate value
        Args:
            value: value to set x to
        Raise:
            TypeError: if value is not int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """getter of y coordinate value"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Setter of the y value
        
        args:
            value (int): y coordinate value
        
        Raise:
            TypeError: if the input is not int
            ValueError: if the input < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """
        Methode that returns the area value of rectangle
        """
        return self.height * self.width
    

    def display(self):
        """
        Method that displays the rectangle with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """
        Methode that override and returns a representation
        of Rectangle -->>(<id>) <x>/<y> - <width>/<height>
        """
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {w}/{h}"
    
    def update(self, *args):
        """
        Methode that updates the order of the parameters passed
        
        Args:
            *args: no-keyworded arguments
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)