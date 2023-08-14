"""Test of file_reader.py"""

# pylint: disable=import-error
import os
import pandas as pd
import pytest
from utilities import FileReader

def test_file_reader_init():
    """Test that the object initializes with the correct file path"""
    # Test that the object initializes with the correct file path
    reader = FileReader("test_path.csv")
    assert reader.file_path == "test_path.csv"
    reader2 = FileReader()
    assert reader2.file_path == os.getenv("dataset_path")

def test_read_csv_pdf(tmp_path):
    """Test read csv as pdf"""
    # Test that file is read as a Pandas dataframe and that the conntent matches
    tmp_file = tmp_path / "tmp_file.csv"
    tmp_dict = {"col1":  ["1", "2", "3"], "col2":  ["A", "B", "C"]}
    pdf = pd.DataFrame(tmp_dict)

    print(pdf)
    pdf.to_csv(tmp_file)
    reader = FileReader(tmp_file)
    assert isinstance(reader.read_csv_pdf(), pd.DataFrame)
    assert reader.read_csv_pdf()["col1"].tolist() == [1, 2, 3]
