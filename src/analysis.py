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


# inherits from DatabaseAnalyzer
class FunctionFitter(DatabaseAnalyzer):
    """
    in this class we Select the best 4 ideal functions by minimizing Least-Square Error.
    Inherits from DatabaseAnalyzer.
    """
    def __init__(self, db_name: str = "assignment_data.db"):
        super().__init__(db_name) # Calls parent __init__
        self.train_df = self._load_data_from_db("train_data")
        self.ideal_df = self._load_data_from_db("ideal_data")
        self.best_matches: dict = {}
        self.max_deviations: dict = {}

    def find_best_functions(self) -> tuple[dict, dict]:
        """
        this class Calculates the Sum of Squared Errors (SSE) for each training
        function against all 50 ideal functions to find the best fit..

        Returns:
            tuple[dict, dict]: A tuple containing:
                - best_matches: {train_col: ideal_col}
                - max_deviations: {train_col: max_dev}
        """
        print("Finding best functions via Least-Square Error...")
        
        # Align data on 'x' for accurate comparison
        train = self.train_df.set_index('x')
        ideal = self.ideal_df.set_index('x')
        common_x = train.index.intersection(ideal.index)
        
        train_aligned = train.loc[common_x]
        ideal_aligned = ideal.loc[common_x]

        train_cols = [f'y{i}' for i in range(1, 5)] # y1-y4
        ideal_cols = [f'y{j}' for j in range(1, 51)] # y1-y50
        
        for train_col in train_cols:
            min_sse = np.inf
            best_fit = None
            
            for ideal_col in ideal_cols:
                sse = np.sum((train_aligned[train_col] - ideal_aligned[ideal_col])**2)
                if sse < min_sse:
                    min_sse = sse
                    best_fit = ideal_col
            
            self.best_matches[train_col] = best_fit
            
            # Calculate max deviation for the best pair
            max_dev = np.max(np.abs(train_aligned[train_col] - ideal_aligned[best_fit]))
            self.max_deviations[train_col] = max_dev

        print("✅ Best functions found.")
        return self.best_matches, self.max_deviations


