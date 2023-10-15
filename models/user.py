#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with attributes such as
    email, password, first name, and last name.

    Example Usage:
    user = User(email="example@example.com", password="password123",
    first_name="John", last_name="Doe")
    print(user.email)  # Output: example@example.com
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a user object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
