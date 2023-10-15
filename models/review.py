#!/usr/bin/python3
""""""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    framework for the reviews from the user
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)