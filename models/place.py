#!/usr/bin/python3
""""""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Blueprints for the place objects
    """
    city_id = ""
    user_id = ""
    name = ""
    descriptuion = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    pricce_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []