#!/usr/bin/python3
"""File storage class for AirBnB"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: JSON file path
        __objects: stored objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        m_dict = {}
        if cls:
            dictionary = self.__objects
            for k in dictionary:
                m_part = k.replace('.', ' ')
                m_part = shlex.split(m_part)
                if (m_part[0] == cls.__name__):
                    m_dict[k] = self.__objects[k]
            return (m_dict)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """reloads the JSON file
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[k]

    def close(self):
        """ calls reload()
        """
        self.reload()
