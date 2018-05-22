#!/usr/bin/python3
'''
Defines unittests for Base Class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    '''Testing Base class'''

    @classmethod
    def setUpClass(cls):
        '''Test Instances'''
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(12)
        cls.b4 = Base()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4

    def test_base_class_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_base_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b4.id, 3)

    def test_base_init_docstring(self):
        self.assertIsNotNone(Base.__init__.__doc__)

    def test_base_to_json_string_docstring(self):
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_base_from_json_string_docstring(self):
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_base_create_docstring(self):
        self.assertIsNotNone(Base.create.__doc__)

    def test_base_save_to_file_docstring(self):
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_base_load_from_file_docstring(self):
        self.assertIsNotNone(Base.load_from_file.__doc__)


if __name__ == '__main__':
    unittest.main()
