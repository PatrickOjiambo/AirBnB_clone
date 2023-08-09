#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model_json = my_model.to_dict()
my_new_model = BaseModel(**my_model_json)

print(my_new_model)