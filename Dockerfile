# Step 1: Use an official Python base image
FROM python:3.10-slim

# Step 2: Set environment variables
# Prevents Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory inside the container
WORKDIR /app

# Step 4: Copy the application files to the container
COPY . /app

# Step 5: Install system dependencies and Python dependencies
RUN apt-get update && apt-get install -y \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Step 6: Set up a virtual environment and install requirements
RUN python -m venv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install -r requirements.txt

# Step 7: Expose port 3000 for the application
EXPOSE 3000

# Step 8: Run the application with Waitress on port 9000
CMD ["./venv/bin/python", "-m", "waitress", "serve", "app:app", "--listen=0.0.0.0:9000"]
