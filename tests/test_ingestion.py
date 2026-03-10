import pandas as pd
import os
import pytest

@pytest.fixture
def mock_data_file():
    # Setup: Create a tiny file for the test
    df = pd.DataFrame({'name': ['Alice', 'Bob']})
    df.to_csv("test_data.csv", index=False)
    yield "test_data.csv"
    # Teardown: Remove the file after test
    os.remove("test_data.csv")

def test_raw_data_has_columns(mock_data_file):
    # Act: Read the file we just created
    df = pd.read_csv(mock_data_file)
    
    # Assert
    assert "name" in df.columns
    assert len(df) == 2