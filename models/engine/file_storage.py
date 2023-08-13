#!/usr/bin/python3
"""
This module contains the process of serialization
and deserialisation of instances to instances and back.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
                

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as file:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, file)

    


    def reload(self):
        
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the
        file doesn't exist, no exception should be raised)
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in data.items()}
        except Exception:
            pass
              
        

