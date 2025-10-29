# tests/test_db_loader.py

import unittest
import os
import pandas as pd
from sqlalchemy import create_engine, inspect
from unittest.mock import patch, MagicMock

# Add src to path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.db_loader import DatabaseLoader
from src.exceptions import DataLoadError

class TestDatabaseLoader(unittest.TestCase):
    """
    this class tests the DatabaseLoader class.
    """
    
    def setUp(self):
        """Set up a temporary database and dummy CSV."""
        self.db_name = "test_loader.db"
        self.csv_path = "test_dummy.csv"
        
        # Ensure old test DB is gone
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        
        # Create a dummy CSV file
        df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
        df.to_csv(self.csv_path, index=False)
        
        # Create the loader for the tests
        self.loader = DatabaseLoader(self.db_name)

    @patch('src.db_loader.pd.read_csv')
    def test_load_csv_file_not_found(self, mock_read_csv):
        """
        this tests that our custom DataLoadError is raised when a CSV is not found
        """
        mock_read_csv.side_effect = FileNotFoundError("File missing")
        
        # Expect a DataLoadError
        with self.assertRaises(DataLoadError):
            self.loader.load_csv_to_table("bad_path.csv", "bad_table")

    def test_load_csv_to_table_success(self):
        """Tests that a CSV is correctly loaded into the database."""
        self.loader.load_csv_to_table(self.csv_path, "dummy_table")
        
        # Check that the table was created and has the right data
        # Get the engine from the loader we already created
        engine = self.loader.engine
        
        # Use SQLAlchemy inspector to check if table exists
        inspector = inspect(engine)
        self.assertIn("dummy_table", inspector.get_table_names())
        
        # Read data back to check content
        loaded_df = pd.read_sql("SELECT * FROM dummy_table", engine)
        self.assertEqual(len(loaded_df), 2)
        self.assertEqual(loaded_df.iloc[0]['x'], 1)

  """  def tearDown(self):
        """Clean up the dummy files."""
        # Close the connection FIRST to release the file lock
        if self.loader:
            self.loader.close()
        
        # Now we can safely delete the files
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
"""
if __name__ == '__main__':
    unittest.main()