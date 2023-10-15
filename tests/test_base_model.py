import unittest
from models.base_model import BaseModel
from datetime import datetime

class   TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""
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

    def test_to_dict(self):
        """Tests the to dict"""
        self.assertEqual(dict, type(self.base.to_dict()))

    def test_kwargs(self):
        """Tests the kwargs"""
        base2 = BaseModel(**self.base.to_dict())
        self.assertEqual(self.base.id, base2.id)
        self.assertEqual(self.base.created_at, base2.created_at)
        self.assertEqual(self.base.updated_at, base2.updated_at)
        self.assertNotEqual(self.base, base2)