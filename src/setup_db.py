import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def init_db():
    # Use echo=True to see the actual SQL being sent to the DB
    engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
    
    with engine.connect() as conn:
        print("Executing CREATE TABLE...")
        conn.execute(text("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));"))
        conn.execute(text("""INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie'), ('Dave'), ('Eve'), ('Frank');"""))
        conn.commit() # Crucial: force the commit
        print("Success: Table created and data inserted.")

if __name__ == "__main__":
    init_db()