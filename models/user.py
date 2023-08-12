#!/usr/bin/python3
"""Contains code for the User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class that manages the user entity"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""