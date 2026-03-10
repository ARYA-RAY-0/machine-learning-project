import pandas as pd

# The "Unit" - This is pure logic. No files involved, making it perfect for tests.
def clean_data_logic(df):
    df = df.copy() 
    df['name'] = df['name'].str.lower().str.strip()
    df['name_length'] = df['name'].apply(len)
    return df

# The "Wrapper" - Handles the actual file system interactions.
def preprocess_data(input_path="data/raw_data.csv", output_path="data/processed_data.csv"):
    if not input_path:
        raise FileNotFoundError("Input path is required.")
        
    df = pd.read_csv(input_path)
    cleaned_df = clean_data_logic(df)
    cleaned_df.to_csv(output_path, index=False)
    print(f"Success! Cleaned data saved to {output_path}")