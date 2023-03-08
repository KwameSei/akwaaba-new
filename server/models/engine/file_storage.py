#!/usr/bin/python3
"""
Contains the FileStorage class model
"""
import json
from models.base_model import BaseModel
from models.user import User
#from models.state import State
#from models.amenity import Amenity
#from models.city import City
#from models.place import Place
#from models.review import Review
from os import path


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """
        Returning all the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, new_obj):
        """
        creates into __objects the object with it's key <obj class name>.id
        Example: user.123456
        """
        key = new_obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, new_obj.id)] = new_obj

    def save(self):
        """
        Save to serialize __objects to the JSON file
        """
        with open(FileStorage.__file_path, mode="w", encoding="utf") as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        if path.exists(FileStorage.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    FileStorage.__objects[key] = \
                            eval(value['__class__'])(**value)
