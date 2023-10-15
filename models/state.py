#!/usr/bin/python3
"""
This code snippet defines a class called `State` that represents a framework for object state. It inherits from the `BaseModel` class and has a single attribute called `name`. The class overrides the `__init__` method from the `BaseModel` class.

Example Usage:
    state = State(name="California")
    print(state.name)  # Output: California

Inputs:
    - name (string): The name of the state.

Outputs:
    - None. The code snippet does not produce any output when executed.
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    framework for object state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)