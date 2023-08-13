"""
This module provides a FileReader class to read data from various file formats.
"""

# pylint: disable=import-error
import os
import pandas as pd
from dotenv import load_dotenv


class FileReader:
    """This module loads files as pdf, np array, etc."""

    def __init__(self, file_path=None):
        self.file_path = file_path
        if self.file_path is None:
            load_dotenv()
            self.file_path = os.getenv("dataset_path")

    def read_csv_pdf(self):
        """Read csv file as Pandas dataframe."""
        try:
            pdf = pd.read_csv(self.file_path)
            return pdf
        except Exception as exeption:
            print(f"Error reading the file: {exeption}")
            return None