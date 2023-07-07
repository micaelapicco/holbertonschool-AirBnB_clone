#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""

import unittest
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """Test of Class BaseModel"""

    def test_str(self):
        """Checks if name is an empty string"""
        test = BaseModel()
        compare = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertEqual(str(test), compare)


if __name__ == '__main__':
    unittest.main()
