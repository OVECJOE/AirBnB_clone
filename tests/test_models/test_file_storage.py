#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest

import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Contains test cases against the FileStorage class"""

    def setUp(self) -> None:
        self.dummy_storage = FileStorage()

    def test_file_path_and_objects_are_a_not_public(self):
        """Checks that file_path and objects are a private class attribute"""
        self.assertNotIn("__file_path", FileStorage.__dict__.keys())
        self.assertNotIn("__objects", FileStorage.__dict__.keys())

    def test_all_method_returns_the_objects_class_attr(self):
        """Checks that dummy_storage.all() returns __objects"""
        self.assertEqual(type(self.dummy_storage.all()), dict)
        self.assertIs(self.dummy_storage.all(),
                      self.dummy_storage._FileStorage__objects)

    def test_that_new_method_works_as_expected(self):
        """Checks that dummy_storage.all() works as expected"""
        new = BaseModel()
        self.dummy_storage.new(new)
        self.assertEqual(self.dummy_storage.all()["BaseModel.{}".format(new.id)],
                         new)
        del self.dummy_storage.all()["BaseModel.{}".format(new.id)]

    def test_that_the_storage_variable_has_been_declared(self):
        """Checks that storage has been declared in models/__init__.py"""
        self.assertTrue(type(models.storage) is FileStorage)
