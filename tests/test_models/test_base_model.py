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
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))

        self.assertEqual(type(test.created_at), datetime)
        self.assertEqual(type(test.updated_at), datetime)
        self.assertEqual(type(test.id), str)

    def test_to_dict(self):
        """
        Checks the type to returns to dict
        and if created and updated are str
        """
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

    def test_save(self):
        """Tests the function save"""
        test = BaseModel()
        test.save()
        self.assertEqual(str(test.updated_at)[:20], str(datetime.now())[:20])

    def test_setattr(self):
        """Tests for manually setted attributes"""
        test = BaseModel

        test.string = "a string"
        test.integer = 1
        test.float_num = 1.1
        test.float_inf = float("inf")
        test.flan = float("nan")
        test.empty_list = []
        test.dictionary = {}
        test.boo = True

        self.assertTrue(hasattr(test, "string"))
        self.assertTrue(hasattr(test, "integer"))
        self.assertTrue(hasattr(test, "float_num"))
        self.assertTrue(hasattr(test, "float_inf"))
        self.assertTrue(hasattr(test, "flan"))
        self.assertTrue(hasattr(test, "empty_list"))
        self.assertTrue(hasattr(test, "dictionary"))
        self.assertTrue(hasattr(test, "boo"))

        self.assertTrue(test.string == "a string")
        self.assertTrue(test.integer == 1)
        self.assertTrue(test.float_num == 1.1)
        self.assertTrue(test.float_inf == float("inf"))
        self.assertTrue(test.flan != float("nan"))
        self.assertTrue(test.empty_list == [])
        self.assertTrue(test.dictionary == {})
        self.assertTrue(test.boo is True)


if __name__ == '__main__':
    unittest.main()
