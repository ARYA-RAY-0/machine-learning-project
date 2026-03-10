import os
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv

# This loads the .env file into the environment
load_dotenv()

def ingest_data():
    # Now it pulls from the .env file!
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        raise ValueError("DATABASE_URL not set in .env file")
        
    engine = sqlalchemy.create_engine(db_url)
    print("Connecting to database...")
    query = "SELECT * FROM users" 
    df = pd.read_sql(query, engine)
    
    # Save raw data
    df.to_csv("data/raw_data.csv", index=False)
    print("Data ingested and saved to data/raw_data.csv")

if __name__ == "__main__":
    ingest_data()