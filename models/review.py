#!/usr/bin/python3
""""""
from models.base_model import BaseModel

class review(BaseModel):
    """
    framework for the reviews from the user
    """
    place_id = ""
    user_id = ""
    text = ""