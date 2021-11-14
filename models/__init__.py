#!/usr/bin/python3
"""
__init__ dunder method for the models directory
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
