import pandas as pd
import os

def preprocess_data(input_path="data/raw_data.csv", output_path="data/processed_data.csv"):
    print("Loading raw data...")
    df = pd.read_csv(input_path)
    
    # 1. Simple cleaning: lowercasing and stripping whitespace
    df['name'] = df['name'].str.lower().str.strip()
    
    # 2. Dummy Feature Engineering: Adding a length feature
    df['name_length'] = df['name'].apply(len)
    
    # 3. Saving processed output
    df.to_csv(output_path, index=False)
    print(f"Success! Cleaned data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()