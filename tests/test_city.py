import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test for City class"""
    def setUp(self):
        """Sets up the class"""
        self.city = City()

    def tearDown(self):
        """Tears down the class"""
        del self.city

    def test_name(self):
        """Tests the name"""
        self.assertEqual(str, type(self.city.name))

    def test_state_id(self):
        """Tests the state id"""
        self.assertEqual(str, type(self.city.state_id))

    def test_str(self):
        """Tests the str"""
        self.assertEqual(str, type(self.city.__str__()))

    def test_to_dict(self):
        """Tests the to dict"""
        self.assertEqual(dict, type(self.city.to_dict()))

    def test_kwargs(self):
        """Tests the kwargs"""
        city2 = City(**self.city.to_dict())
        self.assertEqual(self.city.id, city2.id)
        self.assertEqual(self.city.created_at, city2.created_at)
        self.assertEqual(self.city.updated_at, city2.updated_at)
        self.assertNotEqual(self.city, city2)