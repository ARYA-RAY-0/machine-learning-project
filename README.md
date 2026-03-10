ML-Pipeline-Name-Inference-Service
An end-to-end production-grade MLOps pipeline designed to ingest user data from a PostgreSQL database, perform automated feature engineering, train a logistic regression model, and serve predictions via a FastAPI service.

🚀 Key Features
Automated Orchestration: Pipeline managed via DVC for reproducible data workflows.

Experiment Tracking: Model performance and metrics logged with MLflow.

Containerized Deployment: API served through a Docker container, ensuring environment parity.

REST API: Real-time inference via FastAPI.

🛠 Tech Stack
Language: Python 3.12

ML: Scikit-Learn, MLflow

Data: PostgreSQL, Pandas, SQLalchemy

DevOps: DVC, Docker, FastAPI

💻 How to run this
Clone the repo: git clone <your-repo-url>

Build the API: docker build -t my-ml-api .

Run the service: docker run -p 8000:8000 my-ml-api

Predict: Visit http://127.0.0.1:8000/predict/Alice
