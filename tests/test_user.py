import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test for User class"""
    def setUp(self):
        """Sets up the class"""
        self.user = User()

    def tearDown(self):
        """Tears down the class"""
        del self.user

    def test_email(self):
        """Tests the email"""
        self.assertEqual(str, type(self.user.email))

    def test_password(self):
        """Tests the password"""
        self.assertEqual(str, type(self.user.password))

    def test_first_name(self):
        """Tests the first name"""
        self.assertEqual(str, type(self.user.first_name))

    def test_last_name(self):
        """Tests the last name"""
        self.assertEqual(str, type(self.user.last_name))

    def test_str(self):
        """Tests the str"""
        self.assertEqual(str, type(self.user.__str__()))

    def test_to_dict(self):
        """Tests the to dict"""
        self.assertEqual(dict, type(self.user.to_dict()))

    def test_kwargs(self):
        """Tests the kwargs"""
        user2 = User(**self.user.to_dict())
        self.assertEqual(self.user.id, user2.id)
        self.assertEqual(self.user.created_at, user2.created_at)
        self.assertEqual(self.user.updated_at, user2.updated_at)
        self.assertNotEqual(self.user, user2)