# main.py

"""
This script orchestrates the full pipeline:
1.  Uses DatabaseLoader (with SQLAlchemy) to load CSVs into a SQLite DB.
2.  Uses FunctionFitter (with sqlite3) to find the 4 best functions.
3.  Uses TestDataMapper (with sqlite3) to map test data.
4.  Saves the mapped results back to the database.
5.  Uses Plotter (with Bokeh) to generate the final visualization.

This classes are object-oriented, uses inheritance, includes custom
exceptions, and uses all required libraries (SQLAlchemy, Pandas, Bokeh)
"""
import sys
from src.db_loader import DatabaseLoader
from src.analysis import FunctionFitter, TestDataMapper
from src.plotter import generate_plots
from src.exceptions import DataPipelineError

# Define the database name to be used by all modules
DATABASE_FILE = "assignment_pipeline.db"

def main_pipeline():
    """
    Executes the full data processing and analysis pipeline.
    """
    try:
        # --- Step 1: Load Data into Database ---
        # This step uses SQLAlchemy
        print("--- Step 1: Loading Data into Database ---")
        loader = DatabaseLoader(db_name=DATABASE_FILE)
        loader.run_initial_load()

        # --- Step 2: Fit Functions (Least Squares) ---
        print("\n--- Step 2: Fitting Ideal Functions ---")
        fitter = FunctionFitter(db_name=DATABASE_FILE)
        best_matches, max_deviations = fitter.find_best_functions()
        
        print("\nBest Matches Found:")
        for train, ideal in best_matches.items():
            print(f"  {train} -> {ideal} (Max Dev: {max_deviations[train]:.4f})")
        fitter.close()

        # ---- Step 3: Map Test Data (sqrt(2) Rule) ----
        print("\n--- Step 3: Mapping Test Data ---")
        mapper = TestDataMapper(best_matches, max_deviations, db_name=DATABASE_FILE)
        mapped_df = mapper.map_test_points()
        
        # --- Step 4: Save Mapped Results ---
        print("\n--- Step 4: Saving Mapped Results to DB ---")
        mapper.save_results_to_db(mapped_df)
        print("\nSample of Mapped Data:")
        print(mapped_df.head())
        mapper.close()

        # --- Step 5: Generate Visualizations ---
        # This step uses Bokeh
        print("\n--- Step 5: Generating Visualizations ---")
        generate_plots(best_matches, db_name=DATABASE_FILE)
        
        print("\n--- Pipeline Finished Successfully. ---")

    except DataPipelineError as e:
        print(f"\n--- A PIPELINE ERROR OCCURRED ---", file=sys.stderr)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n--- AN UNEXPECTED ERROR OCCURRED ---", file=sys.stderr)
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main_pipeline()