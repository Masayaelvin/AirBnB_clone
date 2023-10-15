import unittest
from models.state import State
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_initialization(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")