#!/usr/bin/python3
"""class TestState tester for Review"""
import unittest
from models.review import Review
x = Review()


class TestReview(unittest.TestCase):
    """Test for BM.user.py"""

    def test_place_id(self):
        """Checks that the place id is a str"""
        self.assertTrue(type(x.place_id) == str)

    def test_user_id(self):
        """Checks that the user id is a str"""
        self.assertTrue(type(x.user_id) == str)

    def test_text(self):
        """Checks that the text is a str"""
        self.assertTrue(type(x.text) == str)


if __name__ == '__main__':
    unittest.main()