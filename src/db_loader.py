# src/db_loader.py
"""
this file Manages the initial database creation and the dat-loading using SQLAlchemy.
This class is responsible for populating the SQLite database from CSV files for our project.
"""

import pandas as pd
from sqlalchemy import create_engine
from .exceptions import DataLoadError, DatabaseConnectionError

class DatabaseLoader:
    """
    this class Handles loading all CSV files into a central SQLite database.
    It uses SQLAlchemy to create the engine and write data.
    """
    
    def __init__(self, db_name: str = "assignment_data.db"):
        """
        Initializes the loader by creating a SQLAlchemy engine.

        Args:
            db_name (str): The file name for the SQLite database.
        """
        try:
            self.db_name = db_name
            self.engine = create_engine(f"sqlite:///{db_name}")
            print(f"DatabaseLoader initialized with engine for '{db_name}'.")
        except Exception as e:
            raise DatabaseConnectionError(e)

    def load_csv_to_table(self, csv_path: str, table_name: str):
        """
        Reads a CSV file using pandas and loads it into the table
        in the SQLite database using the SQLAlchemy engine.

        Args:
            csv_path (str): Path to the source CSV file.
            table_name (str): Name of the target table in the database.
        
        Raises:
            DataLoadError: If the CSV file is not found or if the
                           database write operation fails.
        """
        try:
            print(f"Loading '{csv_path}' into table '{table_name}'...")
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            print(f"✅ Successfully loaded data into '{table_name}'.")
        except FileNotFoundError as e:
            raise DataLoadError(csv_path, e)
        except Exception as e:
            # Catches pandas.to_sql errors
            raise DataLoadError(f"table {table_name}", e)

    def run_initial_load(self):
        """
        An easy method to load all required data files at once.
        """
        self.load_csv_to_table("data/train.csv", "train_data")
        self.load_csv_to_table("data/ideal.csv", "ideal_data")
        self.load_csv_to_table("data/test.csv", "test_data")
        print("--- All data loaded into database. ---")
    