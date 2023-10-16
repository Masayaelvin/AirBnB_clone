#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
    framework from the object city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
