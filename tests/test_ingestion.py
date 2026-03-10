import os
import pandas as pd

def test_raw_data_exists():
    # Check if the file exists
    assert os.path.exists("data/raw_data.csv")

def test_raw_data_has_columns():
    # Check if the data has the columns we need
    df = pd.read_csv("data/raw_data.csv")
    assert "name" in df.columns
    assert len(df) > 0