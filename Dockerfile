# Lightweight production image
FROM python:3.10-slim

WORKDIR /app

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source and configurations
COPY config/ ./config/
COPY src/ ./src/
COPY data/ ./data/

# Run the pipeline
CMD ["python", "src/main.py"]
