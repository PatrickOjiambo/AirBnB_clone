#!/usr/bin/python3
"""
This module contains the process of serialization
and deserialisation of instances to instances and back.
"""
import json
import os
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
        with open(self.__file_path, "a") as file:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        classes = {
            "BaseModel": BaseModel()
        }
        return classes

    def reload(self):
        
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the
        file doesn't exist, no exception should be raised)
        """
        # if os.path.exists(FileStorage.__file_path):
        #     with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
        #         my_return = json.load(file)
        #         my_return = {key: self.classes()[value["__class__"]](**value) for key, value in obj_dict.items()}
        #         FileStorage.__objects = my_return                
        # else:
        #     return
        pass
    
    def object_setter(self, object):
        """Setter for the variable __objects"""
        FileStorage.__objects = object
        
        

