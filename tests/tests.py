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
    
    def test_kwargs(self):
        base6 = BaseModel()
        base7 = BaseModel(**base6.to_dict())
        self.assertEqual(base6.to_dict(), base7.to_dict())
    
    def test_kwargs_none(self):
        base8 = BaseModel(None)
        base9 = BaseModel(None)
        self.assertNotEqual(base8.id, base9.id)
    
    def test_to_dict(self):
        base10 = BaseModel()
        self.assertEqual(type(base10.to_dict()), dict)
    
    def test_to_dict_class(self):
        base11 = BaseModel()
        self.assertEqual(base11.to_dict()['__class__'], 'BaseModel')



if __name__ == "__main__":
    unittest.main()
