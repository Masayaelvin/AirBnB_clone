#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        my_model = BaseModel()
        to_dict = my_model.to_dict
        self.assertNotEqual(type(my_model), type(to_dict))

if __name__ == "__main__":
    unittest.main()
