#/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def test_file_path(self):
        """Test file_path attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects(self):
        """Test objects attribute"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """Test all method"""
        self.assertEqual(dict, type(FileStorage().all()))

    def test_new(self):
        """Test new method"""
        fs = FileStorage()
        fs.new(BaseModel())
        self.assertIn(BaseModel(), fs.all().values())


if __name__ == "__main__":
	unittest.main()
