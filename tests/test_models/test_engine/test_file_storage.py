#!/usr/bin/python3
"""
Unittest for class FileStoreage methods
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_file_storage(unittest.TestCase):
    """Class that contains all test for FileStorage"""

    def test_file_path(self):
        """Checks if __file_path is private attribute"""
        test = FileStorage()
        self.assertEqual(test._FileStorage__file_path, 'file.json')

    def test_objects(self):
        """Cheks if objects is a dic and is a private attribute"""
        test = FileStorage()
        self.assertEqual(type(test._FileStorage__objects), dict)

    def test_all(self):
        """Checks if all returns a dictonary"""
        test = FileStorage()
        self.assertEqual(type(test.all()), dict)

    def test_new(self):
        """Checks if a new object is correctly added"""
        test = FileStorage()
        test.all().clear()
        compare = BaseModel()
        test.new(compare)
        self.assertNotEqual(len(test.all()), 0)

    def test_save(self):
        """Cheks if save objects from Base model to test"""
        test = FileStorage()
        test.all().clear()
        compare = BaseModel()
        test.save()
        self.assertNotEqual(len(test.all()), 0)

    def test_reload(self):
        """checks that after calling the reload there are objects loaded"""
        test = FileStorage()
        test.all().clear()
        test.reload()
        self.assertNotEqual(len(test.all()), 0)


if __name__ == '__main__':
    unittest.main()
