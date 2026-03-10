# Use a slim Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (needed for some ML libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy your dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project source code
COPY . .

# Expose the API port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "src.predict:app", "--host", "0.0.0.0", "--port", "8000"]