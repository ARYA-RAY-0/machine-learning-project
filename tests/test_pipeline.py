import pytest
import pandas as pd
from src.preprocessing import clean_data # Assuming you have a clean_data function

def test_data_cleaning():
    # Arrange: Create dummy input
    raw_data = pd.DataFrame({'name': ['Alice', 'Bob']})
    
    # Act: Run your cleaning function
    processed_data = clean_data(raw_data)
    
    # Assert: Verify the output is what you expect
    assert 'length' in processed_data.columns
    assert len(processed_data) == 2