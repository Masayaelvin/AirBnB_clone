#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class Testreviview(unittest.TestCase):
    """
    Test for Review class
    Args:
        unittest (_type_): _description_
    """
    def setUp(self):
        """Sets up the class"""
        self.review = Review()

    def test_attributes(self):
        """Tests the attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))


    def test_initialization(self):
        """Tests the initialization"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_no_args_instantiates(self):
        """Tests the no args instantiates"""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Tests the new instance stored in objects"""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Tests the id is public str"""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Tests the created at is public datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Tests the updated at is public datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """tests that the place Id is a public class attribute"""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """tests that user Id is a public class attribute"""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        """tests that text is a public class attribute """
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        """
        Tests that two reviews have different ids.
        """
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        """tests that the 2 reviews have different created at"""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        """tests that 2 reviews have a different created at"""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        """tests the str representation"""
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        """Tests the args unused"""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Tests the instantiation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)
    
class Testreview(unittest.TestCase):
    """tests the review class"""

    # create an instance of review class
    def test_create_instance(self):
        """tests that its an instance of the class"""
        review_instance = Review()
        assert isinstance(review_instance, Review)

    # set place_id, user_id and text attributes of review instance
    def test_set_attributes(self):
        """tests the attributes set are equal to the ones"""
        review_instance = Review()
        review_instance.place_id = "123"
        review_instance.user_id = "456"
        review_instance.text = "This is a review"
        assert review_instance.place_id == "123"
        assert review_instance.user_id == "456"
        assert review_instance.text == "This is a review"

