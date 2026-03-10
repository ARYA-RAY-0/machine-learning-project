import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
from sklearn.linear_model import LogisticRegression

def train_model():
    df = pd.read_csv("data/processed_data.csv")
    
    
    X = df[['name_length']]
    y = [1 if i % 2 == 0 else 0 for i in range(len(df))]
    
    
    print(f"DEBUG: X samples: {len(X)}, y samples: {len(y)}")
    
    with mlflow.start_run():
        model = LogisticRegression()
        print(f"DEBUG: Dataframe head: {df.head()}")
        print(f"DEBUG: Unique classes in y: {set(y)}")
        model.fit(X, y)
        
        
        
        
        # Save the model artifact
        joblib.dump(model, "model.pkl")
        
        # Log to MLflow
        mlflow.sklearn.log_model(model, "model")
        print("Training complete. Model saved as model.pkl")

if __name__ == "__main__":
    train_model()