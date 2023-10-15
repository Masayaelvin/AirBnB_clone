#!/usr/bin/python3
"""
This code snippet defines a class called "Review" that represents a
framework for user reviews. It inherits from the "BaseModel" class and has
attributes for place_id, user_id, and text.

Example Usage:
    review = Review(place_id="123", user_id="456", text="Great place!")
    print(review.place_id)  # Output: 123
    print(review.user_id)  # Output: 456
    print(review.text)  # Output: Great place!

Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who wrote the review.
    text (str): The text content of the review.

Methods:
    __init__(self, *args, **kwargs): Initializes a review object with optional arguments.

    Note: This class inherits the "__init__" method from the "BaseModel" class and calls it using the "super()" function.

"""
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