#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """Test of Class BaseModel"""

    def test_attributes_type(self):
        """checks the types of attributes"""
        test = BaseModel()
        self.assertEqual(type(test.created_at), datetime)
        self.assertEqual(type(test.updated_at), datetime)
        self.assertEqual(type(test.id), str)

    def test_to_dict(self):
        """Checks the type to returns to dict and if created and updated are str"""
        instance = BaseModel()
        test = instance.to_dict()
        self.assertEqual(type(test), dict)
        self.assertEqual(type(test["created_at"]), str)
        self.assertEqual(type(test["updated_at"]), str)

    def test_str(self):
        """Checks if name is an empty string"""
        test = BaseModel()
        compare = f"[{test.__class__.__name__}] ({test.id}) {test.__dict__}"
        self.assertEqual(str(test), compare)


if __name__ == '__main__':
    unittest.main()
