#!/usr/bin/python3
"""Creates a unique FileStorage instance for the application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from os import getenv
from models.place import Place
from models.engine.db_storage import DBStorage


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
