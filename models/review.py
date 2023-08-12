#!/usr/bin/python3
"""Contains code for the Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Class that manages the review entity"""
    place_id = ""
    user_id = ""
    text = ""