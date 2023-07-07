#!/usr/bin/python3
"""
Unittest for class FileStoreage methods
"""

import unittest
from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel


class Test_file_storage(unittest.TestCase):
    """Class that contains all test for FileStorage"""

    def test_file_path(self):
        """Checks if __file_path is private attribute"""
        test = FileStorage()
        self.assertEqual(test._FileStorage__file_path, 'Objects.json')

    def test_objects(self):
        """Cheks if objects is a dic and is a private attribute"""
        test = FileStorage()
        self.assertEqual(type(test._FileStorage__objects), dict)

    def test_all(self):
        """Checks if all returns a dictonary"""
        test = FileStorage()
        self.assertEqual(type(test.all()), dict)

    # def test_save(self):
