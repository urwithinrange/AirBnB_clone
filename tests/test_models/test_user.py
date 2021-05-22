#!/usr/bin/python3
"""class TestState tester for User"""
import unittest
from models.user import User

x = User()


class TestUser(unittest.TestCase):
    """Test for BM.user.py"""

    def test_first_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.first_name) == str)

    def test_last_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.last_name) == str)

    def test_email(self):
        """Checks that the email is a str"""
        self.assertTrue(type(x.email) == str)

    def test_password(self):
        """Checks that the password is a str"""
        self.assertTrue(type(x.password) == str)


if __name__ == '__main__':
    unittest.main()