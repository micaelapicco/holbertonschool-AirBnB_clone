#!/usr/bin/python3
"""Contains tests for class State"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for class State"""

    def test_type(self):
        """Checks for the correct type"""
        state = State()
        self.assertIsInstance(state, State)
