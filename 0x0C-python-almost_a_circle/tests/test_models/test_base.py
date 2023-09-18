import unittest
from models.base import Base

class test_base(unittest.TestCase):
    """Unit test for the Base class"""

    def setUp(self):
        """Methode to run before each test"""
        Base.__nb_objects = 0
    
    def test_id(self):
        """Methode that checks the id instance attribute"""

        b = Base()
        self.assertEqual(b.id, 1)

        b = Base()
        self.assertEqual(b.id, 2)

        b = Base(12)
        self.assertEqual(b.id, 12)

        b = Base()
        self.assertEqual(b.id, 3)