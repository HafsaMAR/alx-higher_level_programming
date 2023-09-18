import unittest
from contextlib import redirect_stdout
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

"""Module to test the rectangle and Base classes"""


class test_Rectangle(unittest.TestCase):
    """Unit test for the Rectangle class"""

    def setUp(self):
        """Methode to run before each test"""
        Base._Base__nb_objects = 0
    
    def test_id(self):
        """Methode that checks the id instance attribute"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
    
    def test_width(self):
        """Validate the width attribute"""

        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

        r.width = 2
        self.assertEqual(r.width, 2)

        with self.assertRaises(TypeError) as context:
            r = Rectangle("2", 10)
        self.assertEqual(str(context.exception), "width must be an integer")
        
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-1, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 5)
        self.assertEqual(str(context.exception), "width must be > 0")
    
    def test_height(self):
        """Validate height attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

        r.height = 2
        self.assertEqual(r.height, 2)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, "h")
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2, "x", 3)
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, -5, 3)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2, 3, "y")
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display(self):

        r = Rectangle(4, 6)
        output = StringIO()
        rectangle = "####\n####\n####\n####\n####\n####"
        with redirect_stdout(output):
            r.display()
        printed_rectangle = output.getvalue().strip()
        self.assertEqual(printed_rectangle, rectangle)
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        output = r1.__str__()
        self.assertEqual(output, "[Rectangle] (12) 2/1 - 4/6")

        r1 = Rectangle(5, 5, 1)
        output = r1.__str__()
        self.assertEqual(output, "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update(height=1)
        self.assertEqual(r2.height, 1)
        r2.update(width=1, x=2)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.x, 2)
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.y, 1)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 10)
        r1.update(89, 2, 3, 4, 5)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5})