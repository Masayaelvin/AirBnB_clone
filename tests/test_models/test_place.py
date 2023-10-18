#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""
    def setUp(self):
        """Sets up the class"""
        self.place = Place()

    def test_no_args_instantiates(self):
        """tests no args"""
        self.assertEqual(Place, type(Place()))

    def test_id_is_public_str(self):
        """tests tat id is a str"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """tests that created at is a public datetime"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """tests that updated at is a public datetime"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        "" "tests that city id is a public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        "" "tests that user id is a public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        "" "tests that name is a public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)


    def test_two_places_unique_ids(self):
        """assert that the 2 places have different id's"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        """"assert that the 2 places have different created_at"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        """assert that the 2 places have different updated_at"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        """tests the str representation"""
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        """tests that args are unused"""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """tests instantiation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """tests instantiation with None kwargs"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_attributes(self):
        """tests attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_initialization(self):
        """tests initialization"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_one_save(self):
        """tests one save"""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        """tests two saves"""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_save_with_arg(self):
        """tests save with arg"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        """tests save updates file"""
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())

    def test_to_dict_type(self):
        """tests to_dict type"""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """tests to_dict contains correct keys"""
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """tests to_dict contains added attributes"""
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """tests to_dict datetime attributes are strs"""
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        """tests to_dict output"""
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """tests contrast to_dict dunder dict"""
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        """tests to_dict with arg"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)

if __name__ == '__main__':
    unittest.main()
