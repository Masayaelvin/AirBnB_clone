#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
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

    def test_to_dict(self):
        """Tests the to dict"""
        self.assertEqual(dict, type(self.city.to_dict()))

    def test_no_args_instantiates(self):
        """Tests the no args instantiates"""
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        """Tests the id is public str"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Tests the created at is public datetime"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """makes sure that public Id is public class attribute"""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """tests name is a public class attribute"""
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        """checks that the 2 have unique ID's"""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """checks that the 2 have different created at"""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """checks that the 2 have different updated at"""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """Tests the str representation"""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        """tests unsused args"""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """Tests the instantiation with None kwargs"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """Tests the kwargs"""
        city2 = City(**self.city.to_dict())
        self.assertEqual(self.city.id, city2.id)
        self.assertEqual(self.city.created_at, city2.created_at)
        self.assertEqual(self.city.updated_at, city2.updated_at)
        self.assertNotEqual(self.city, city2)

    def test_one_save(self):
        """tests the save method"""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        """tests the save method"""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        """tests the save method"""
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """tests the save method"""
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

if __name__ == "__main__":
    unittest.main()
