#!/usr/bin/python3
""""""
from models.base_model import BaseModel
class State(BaseModel):
    """
    framework for object state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)