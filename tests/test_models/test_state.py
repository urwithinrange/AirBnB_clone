#!/usr/bin/python3
"""class TestState tester for State"""
import unittest
from models.state import State

x = State()


class TestState(unittest.TestCase):
    """Test for BM.state.py"""

    def test_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.name) == str)


if __name__ == '__main__':
    unittest.main()