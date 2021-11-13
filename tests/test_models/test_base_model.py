#!/usr/bin/python3
"""A module that contains the test suite for the BaseModel class"""
import unittest
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """The test suite for models.base_model.BaseModel"""

    def test_if_BaseModel_instance_has_id(self):
        """Checks that instance has an id assigned on initialization"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_str_representation(self):
        """Checks if the string representation is appropriate"""
        b = BaseModel()
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

    def test_id_is_unique(self):
        """Checks if id is generated randomly and uniquely"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id_is_str(self):
        """Checks that id generated is a str object"""
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_created_at_is_datetime(self):
        """Checks that the attribute 'created_at' is a datetime object"""
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_updated_at_is_datetime(self):
        """Checks that the attribute 'updated_at' is a datetime object"""
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_that_created_at_equals_updated_at_initially(self):
        """Checks that create_at == updated_at at initialization"""
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)

    def test_that_save_func_update_update_at_attr(self):
        """Checks that save() method updates the updated_at attribute"""
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(b.updated_at.microsecond,
                           b.created_at.microsecond, "Greater!")

    def test_if_to_dict_returns_dict(self):
        """Checks if BaseModel.to_dict() returns a dict object"""
        b = BaseModel()
        self.assertTrue(type(b.to_dict()) is dict)

    def test_if_to_dict_returns_class_dunder_method(self):
        """Checks if BaseModel.to_dict() contains __class__"""
        b = BaseModel()
        self.assertTrue("__class__" in b.to_dict())

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """Checks that created_at is stored as a str obj in ISO format"""
        b = BaseModel()
        self.assertEqual(b.to_dict()["created_at"], b.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """Checks that updated_at is stored as a str obj in ISO format"""
        b = BaseModel()
        self.assertEqual(b.to_dict()["updated_at"], b.updated_at.isoformat())

    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """Checks that to_dict() returns the expected number of keys/values"""
        b = BaseModel()
        partial_expectation = {k: v for k, v in b.__dict__.items()
                               if not k.startswith("_")}
        self.assertEqual(len(b.to_dict()), len(partial_expectation) + 1)

    def test_when_kwargs_passed_is_empty(self):
        """Checks that id, created_at and updated_at are automatically
        generated if they're not in kwargs"""
        my_dict = {}
        b = BaseModel(**my_dict)
        self.assertTrue(type(b.id) is str)
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

    def test_when_kwargs_passed_is_not_empty(self):
        """Checks that id, created_at and updated_at are created from kwargs"""
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        b = BaseModel(**my_dict)
        self.assertEqual(b.id, my_dict["id"])
        self.assertEqual(b.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(b.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_kwargs_passed_is_more_than_default(self):
        """Checks BaseModel does not break when kwargs contains more than
        the default attributes"""
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        b = BaseModel(**my_dict)
        self.assertTrue(hasattr(b, "name"))

    def test_new_method_not_called_when_dict_obj_is_passed_to_BaseModel(self):
        """Test that storage.new() is not called when a BaseModel obj is
        created from a dict object"""
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        b = BaseModel(**my_dict)
        self.assertTrue(b not in models.storage.all().values(),
                        f"{models.storage.all().values()}")
        del b

        b = BaseModel()
        self.assertTrue(b in models.storage.all().values())
