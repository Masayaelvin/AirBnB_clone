#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):


    def test_to_dict(self):
        my_model = BaseModel()
        to_dict = my_model.to_dict
        self.assertNotEqual(type(my_model), type(to_dict))
    
    def test_base_model(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        base1 = BaseModel()
        base2 = BaseModel()

        self.assertNotEqual(base1.id, base2.id)

    def test_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_string_repr(self):
        base3 = BaseModel()
        string = f"[{base3.__class__.__name__}] ({base3.id}) {base3.__dict__}"
        self.assertEqual(str(base3), string)

    def test_updates_as(self):
        base4 = BaseModel()
        var1 = base4.updated_at
        time.sleep(1)
        base4.save()
        var2 = base4.updated_at
        self.assertNotEqual(var1, var2)

    def test_args(self):
        base5 = BaseModel(None)
        self.assertNotIn(None, base5.__dict__.values())



if __name__ == "__main__":
    unittest.main()
