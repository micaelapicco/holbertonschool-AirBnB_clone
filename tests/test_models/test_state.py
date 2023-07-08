#!/usr/bin/python3
"""Contains tests for class State"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Tests for class State"""

    def test_type_args(self):
        """Checks for the correct type"""
        state = State()
        self.assertIsInstance(state, State)

        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

        self.assertTrue(type(state.id) == str)
        self.assertTrue(type(state.created_at) == datetime)
        self.assertTrue(type(state.updated_at) == datetime)
        self.assertTrue(type(state.name) == str)

        state.name = "a state"
        self.assertEqual(state.name, "a state")


if __name__ == '__main__':
    unittest.main()
