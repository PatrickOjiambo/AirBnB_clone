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
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}"
        self.__objects[key] = obj
        

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "a") as file:
            content = file.write(json.dumps(self.__objects))

    def reload(self):
        pass
        # """
        # Deserializes the JSON file to __objects (only if the JSON
        # file (__file_path) exists ; otherwise, do nothing. If the
        # file doesn’t exist, no exception should be raised)
        # """
        # if os.path.exists(self.__file_path):
        #     with open(self.__file_path, "r", encoding="utf-8") as file:
        #         content = file.read()
        #         final_string = json.loads(content)
        #         return final_string                              
        # else:
        #     return
    #Below code id for testing
    def tester(self):
        print(self.all())

