#!/usr/bin/python3
"""Implements the user's model"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from the BaseModel class and add user's functionalities"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
