#!/usr/bin/python3
"""Contains code for the City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """Class that manages the city entity"""
    state_id = ""
    name = ""