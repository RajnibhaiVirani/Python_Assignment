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

# Replaces TestMatcher, inherits from DatabaseAnalyzer
class TestDataMapper(DatabaseAnalyzer):
    """
    This class Maps test data points to the 4 chosen ideal functions using
    the sqrt(2) deviation criterion.
    Inherits from DatabaseAnalyzer.
    """
    def __init__(self, best_matches: dict, max_deviations: dict, db_name: str = "assignment_data.db"):
        super().__init__(db_name)
        if not best_matches or not max_deviations:
            raise AnalysisConfigurationError("Must provide best_matches and max_deviations.")
            
        self.test_df = self._load_data_from_db("test_data")
        self.ideal_df = self._load_data_from_db("ideal_data")
        
        # Build the thresholds: {ideal_func_name: max_dev * sqrt(2)}
        self.thresholds = {
            ideal_func: max_deviations[train_func] * np.sqrt(2)
            for train_func, ideal_func in best_matches.items()
        }
        self.chosen_ideal_cols = list(self.thresholds.keys())
        
    def map_test_points(self) -> pd.DataFrame:
        """
        Iterates through test data and maps points that fall within
        the calculated deviation threshold.

        Returns:
            pd.DataFrame: A 4-column DataFrame of mapped points
                          (X, Y, Delta Y, No. of ideal func) [cite: 917].
        """
        print("Mapping test data points...")
        
        # Merge test data with only the 4 chosen ideal functions
        ideal_filtered = self.ideal_df[['x'] + self.chosen_ideal_cols]
        merged_data = pd.merge(self.test_df, ideal_filtered, on='x', how='left')
        
        mapped_rows = []
        
        for _, row in merged_data.iterrows():
            best_fit_func = None
            min_dev = np.inf
            
            for ideal_col in self.chosen_ideal_cols:
                if pd.isna(row[ideal_col]):
                    continue # x-value not in ideal set

                deviation = np.abs(row['y'] - row[ideal_col])
                
                # Checks if it meets the sqrt(2) criterion
                if deviation <= self.thresholds[ideal_col]:
                    if deviation < min_dev:
                        min_dev = deviation
                        best_fit_func = ideal_col
            
            # If a match was found, add it to our list
            if best_fit_func:
                mapped_rows.append({
                    'X (test func)': row['x'],
                    'Y (test func)': row['y'],
                    'Delta Y (test func)': min_dev,
                    'No. of ideal func': best_fit_func
                })
        
        print(f"✅ Mapping complete. {len(mapped_rows)} points mapped.")
        return pd.DataFrame(mapped_rows)

    def save_results_to_db(self, mapped_df: pd.DataFrame):
        """
        Saves the final mapped DataFrame to a new table in the database
        as required.#
        
        Note: This uses the parent's `self.conn` (sqlite3) and pandas,
        not sqlalchemy, to match the sample code's architecture.
        """
        try:
            mapped_df.to_sql("mapped_test_results", self.conn, if_exists='replace', index=False)
            print(f"✅ Saved {len(mapped_df)} mapped results to 'mapped_test_results' table.")
        except Exception as e:
            raise DataLoadError("saving mapped results", e)
