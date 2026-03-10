import pandas as pd
import pytest
from src.preprocessing import clean_data_logic

def test_clean_data_logic():
    # Arrange: Setup dummy data
    data = {'name': ['  Alice  ', 'BOB']}
    df = pd.DataFrame(data)
    
    # Act: Apply the logic
    processed_df = clean_data_logic(df)
    
    # Assert: Verify expected outcomes
    assert processed_df.loc[0, 'name'] == 'alice'
    assert processed_df.loc[1, 'name'] == 'bob'
    assert processed_df.loc[0, 'name_length'] == 5
    assert processed_df.loc[1, 'name_length'] == 3