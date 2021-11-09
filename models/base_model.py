#!/usr/bin/python3
"""A module that implements the BaseModel class"""
import cmd
from uuid import uuid4
from datetime import datetime, timezone


class BaseModel(cmd.Cmd):
    """A class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize the BaseModel class

        Args:
            id (str): an assigned id when the instance is created.
            created_at (datetime): the datetime object representing
            when an instance is created.
            updated_at (datetime): the datetime object representing when an
            instance is created and it will be updated everything the object
            is changed.
        """

        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of BaseModel object."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates 'self.updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """

        for attr in ["created_at", "updated_at"]:
            if attr in self.__dict__:
                self.__dict__[attr] = self.__dict__[attr].isoformat()
        attr_set = {k: v for k, v in self.__dict__.items()
                    if not k.startswith("_")}
        attr_set["__class__"] = type(self).__name__

        return attr_set
