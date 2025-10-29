# src/analysis.py

"""
This file Contains the core logic for function fitting and testing data mapping.
This module uses sqlite3 and pandas for data operations, matching the
architecture of the provided sample code.
"""

import pandas as pd
import sqlite3
import numpy as np
from .exceptions import DataLoadError, AnalysisConfigurationError

# NEW Class for Inheritance 
class DatabaseAnalyzer:
    """
    this is the base class for analysis modules that need to read from the database.
    This provides a common connection and data loading mechanism.
    """
    def __init__(self, db_name: str = "assignment_data.db"):
        """
        Initializes the base analyzer and connects to the database.
        
        Args:
            db_name (str): The path to the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"{self.__class__.__name__} connected to '{self.db_name}'.")
        except sqlite3.Error as e:
            raise DataLoadError(self.db_name, e)

    def _load_data_from_db(self, table_name: str) -> pd.DataFrame:
        """
        Protected method to load a table from the DB into a DataFrame.
        
        Args:
            table_name (str): The name of the table to read.
        
        Returns:
            pd.DataFrame: The contents of the table.
        """
        try:
            return pd.read_sql(f"SELECT * FROM {table_name}", self.conn)
        except pd.errors.DatabaseError as e:
            raise DataLoadError(f"table '{table_name}'", e)

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()
            print(f"{self.__class__.__name__} disconnected from DB.")


