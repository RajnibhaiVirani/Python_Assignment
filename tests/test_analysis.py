# tests/test_analysis.py

"""
Unit tests for FunctionFitter and TestDataMapper.
These tests are isolated and use mock data instead of live database.
"""
import unittest
import pandas as pd
import numpy as np
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.analysis import FunctionFitter, TestDataMapper

class TestFunctionFitter(unittest.TestCase):
    
    # Mock the database connection and data loading
    @patch('src.analysis.DatabaseAnalyzer._load_data_from_db')
    @patch('src.analysis.sqlite3.connect')
    def test_fitter_finds_correct_match(self, mock_connect, mock_load_data):
        """
        Tests the Least-Squares logic in isolation.
        """
        # 1. Create Mock Data
        train_df = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [10, 20, 30], # Perfect match for y2
            'y2': [1, 2, 3], 'y3': [1, 2, 3], 'y4': [1, 2, 3]
        })
        ideal_data = {'x': [1, 2, 3], 'y1': [1, 2, 3], 'y2': [10, 20, 30]}
        for i in range(3, 51):
            ideal_data[f'y{i}'] = [i, i, i]
        ideal_df = pd.DataFrame(ideal_data)

        # 2. Configure Mocks
        # Set the return value for when _load_data_from_db is called
        mock_load_data.side_effect = [train_df, ideal_df] # First call returns train, second returns ideal
        mock_connect.return_value = MagicMock() # Mock the connection object

        # 3. Run Test
        fitter = FunctionFitter(db_name="mock_db")
        best_matches, max_devs = fitter.find_best_functions()

        # 4. Assert
        self.assertEqual(best_matches['y1'], 'y2') # y1(train) should match y2(ideal)
        self.assertEqual(best_matches['y2'], 'y1') # y2(train) should match y1(ideal)
        self.assertAlmostEqual(max_devs['y1'], 0.0) # Deviation for perfect match is 0

if __name__ == '__main__':
    unittest.main()