import unittest
from models.review import review
from models.base_model import BaseModel

class Testreviview(unittest.TestCase):
    def setUp(self):
        self.review = review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_initialization(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    
class Testreview:

    # create an instance of review class
    def test_create_instance(self):
        review_instance = review()
        assert isinstance(review_instance, review)

    # set place_id, user_id and text attributes of review instance
    def test_set_attributes(self):
        review_instance = review()
        review_instance.place_id = "123"
        review_instance.user_id = "456"
        review_instance.text = "This is a review"
        assert review_instance.place_id == "123"
        assert review_instance.user_id == "456"
        assert review_instance.text == "This is a review"

