#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """

        # super().__init__()
        # self.id = str(uuid4())
        # self.created_at = self.updated_at = datetime.now()
        # something doesn't add up here.

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    pass
                else:
                    setattr(self, k, v)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        model.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """

        # attr_set = {k: v for k, v in self.__dict__.items()
        #             if not k.startswith('_')}
        # attr_set["__class__"] = type(self).__name__
        # attr_set["created_at"] = attr_set["created_at"].isoformat()
        # attr_set["updated_at"] = attr_set["updated_at"].isoformat()
        # return attr_set

        # -> instead of changing an argument at a time,
        # we can use an if statement to do it all at once
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
