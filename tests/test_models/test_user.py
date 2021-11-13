#!/usr/bin/python3
"""Test suite for the User class in models.user"""
import unittest

from models.user import User
import models


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_name_is_an_empty_str_and_a_class_attribute(self):
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))
