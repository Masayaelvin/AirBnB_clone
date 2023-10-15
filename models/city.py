#!/usr/bin/python3
"""
This code snippet defines a class called `City` that inherits from the `BaseModel` class.

Example Usage:
    city = City(state_id="123", name="New York")

Inputs:
    - state_id: a string representing the state ID of the city.
    - name: a string representing the name of the city.

Outputs:
    No specific output is mentioned in the code snippet.

Code Analysis:
    1. The `City` class is defined, inheriting from the `BaseModel` class.
    2. The `__init__` method is overridden to initialize the `City` object.
    3. The `super().__init__(*args, **kwargs)` line calls the `__init__` method of the parent class (`BaseModel`), passing any additional arguments and keyword arguments.
    4. The parent class's `__init__` method is responsible for setting the attributes of the `City` object based on the provided keyword arguments.
    5. The `City` object is initialized with the provided `state_id` and `name` attributes.

"""

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