#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
A basemodel module that defines all common 
attributes and methods for other classes.
"""
class BaseModel:
    """
    A basemodel class that defines all common
    attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the baseclass
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.id = str(uuid.uuid4())
                    setattr(self, key, value)
                if self.id in kwargs and kwargs.get(self.id) not in storage.all():
                    
                    storage.new(self)
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    
    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance:
        """
        attributes = self.__dict__.copy()
        attributes["__class__"] = self.__class__.__name__
        attributes["created_at"] = self.created_at.isoformat()
        attributes["updated_at"] = self.updated_at.isoformat()
        return attributes
    def __str__(self):
        """
        Returns a string representation of an object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)



"""
You may have done a mistake to put self.id under if kwargs is not empty. 
Please check on that in the scenario that something breaks.
"""

        