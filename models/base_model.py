#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
A basemodel module that defines all common 
attributes and methods for other classes.
"""
class BaseModel():
    """
    A basemodel class that defines all common
    attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the baseclass
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    
    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance:
        """
        attributes = {**self.__dict__}
        attributes["__class__"] = type(self).__name__
        attributes["created_at"] = attributes["created_at"].isoformat()
        attributes["updated_at"] = attributes["updated_at"].isoformat()
        return attributes
    def __str__(self):
        """
        Returns a string representation of an object
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)



        