#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel class
    Args:
        unittest (_type_): _description_
    """    
    def test_to_dict(self):
        """Tests to_dict method of BaseModel"""
        my_model = BaseModel()
        to_dict = my_model.to_dict
        self.assertNotEqual(type(my_model), type(to_dict))
    
    def test_base_model(self):
        """Tests the BaseModel class"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """Tests the id"""
        base1 = BaseModel()
        base2 = BaseModel()

        self.assertNotEqual(base1.id, base2.id)

    def test_string(self):
        """Tests the string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_string_repr(self):
        """this tests that base model prints a string representation"""
        base3 = BaseModel()
        string = f"[{base3.__class__.__name__}] ({base3.id}) {base3.__dict__}"
        self.assertEqual(str(base3), string)

    def test_updates_as(self):
        """this tests that base model updates as expected"""
        base4 = BaseModel()
        var1 = base4.updated_at
        sleep(1)
        base4.save()
        var2 = base4.updated_at
        self.assertNotEqual(var1, var2)

    def test_args(self):
        """this tests that base model args are expected"""
        base5 = BaseModel(None)
        self.assertNotIn(None, base5.__dict__.values())
    
    def test_kwargs(self):
        """this tests that base model kwargs are expected"""
        base6 = BaseModel()
        base7 = BaseModel(**base6.to_dict())
        self.assertEqual(base6.to_dict(), base7.to_dict())
    
    def test_kwargs_none(self):
        """this tests that base model kwargs are none"""
        base8 = BaseModel(None)
        base9 = BaseModel(None)
        self.assertNotEqual(base8.id, base9.id)
    
    def test_to_dict(self):
        """this tests that base model to_dict is a dict"""
        base10 = BaseModel()
        self.assertEqual(type(base10.to_dict()), dict)
    
    def test_to_dict_class(self):
        """this tests that base model to_dict has a class key"""
        base11 = BaseModel()
        self.assertEqual(base11.to_dict()['__class__'], 'BaseModel')

    def test_no_args_instantiates(self):
        """Tests instantiation with no positional arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """this tests that a new instance of base model is stored in objects"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Tests that BaseModel.id is a public instance attribute of type str."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Tests that BaseModel.created_at is a public instance attribute of type datetime."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """tests for datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """tests that the 2 models are unique"""        
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """tests that the 2 models are different"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def setUp(self):

        """Sets up the class"""
        self.base = BaseModel()

    def tearDown(self):
        """Tears down the class"""
        del self.base

    def test_id(self):
        """Tests the id"""
        self.assertEqual(str, type(self.base.id))

    def test_created_at(self):
        """Tests the created at"""
        self.assertEqual(datetime, type(self.base.created_at))

    def test_updated_at(self):
        """Tests the updated at"""
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_str(self):
        """Tests the str"""
        self.assertEqual(str, type(self.base.__str__()))

    def test_two_models_different_updated_at(self):
        """ensures that the 2 models have different updated_at"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """Tests the str representation"""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """Tests that args are not used."""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """tests instantiation with keyword arguments"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """tests instantiation with None keyword arguments"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """tests instantiation with args and kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)



if __name__ == "__main__":
    unittest.main()
