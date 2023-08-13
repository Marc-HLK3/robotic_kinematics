"""
This module provides a FileReader class to read data from various file formats.
"""

# pylint: disable=import-error
import pandas as pd


class FileReader:
    """This module loads files as pdf, np array, etc."""

    def __init__(self, file_path):
        self.file_path = file_path

    def pdf(self):
        try:
            pdf = pd.read_csv(self.file_path)
            return pdf
        except Exception as e:
            print(f"Error reading the file: {e}")
            return None


if __name__ == "__main__":

    reader = FileReader(file_path="test.csv")
    data = reader.read_csv()
