# src/exceptions.py

"""
Defines a custom user-defined exceptions for the data analysis pipeline.
"""

class DataPipelineError(Exception):
    """Base exception for all errors in the pipeline."""
    pass

class DatabaseConnectionError(DataPipelineError):
    """Raised when connection to the database fails."""
    pass

class DataLoadError(DataPipelineError):
    """Raised when loading data from CSV or DB fails."""
    def __init__(self, source, original_exception):
        self.source = source
        self.original_exception = original_exception
        message = f"Failed to load data from {source}. Error: {original_exception}"
        super().__init__(message)

class AnalysisConfigurationError(DataPipelineError):
    """Raised if analysis is running without required data."""
    pass