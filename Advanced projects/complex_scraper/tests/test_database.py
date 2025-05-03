"""
Tests for the database functionality.
"""

import unittest
from storage.database import DatabaseStorage

class TestDatabaseStorage(unittest.TestCase):
    def setUp(self):
        self.connection_string = "sqlite:///test.db"
        self.storage = DatabaseStorage(self.connection_string)
        
    def test_save_data(self):
        """Test saving data to the database."""
        test_data = {"key": "value"}
        self.storage.save(test_data)
        
    def test_get_data(self):
        """Test retrieving data from the database."""
        query = "SELECT * FROM test"
        result = self.storage.get(query)
        self.assertIsNotNone(result) 