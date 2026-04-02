# -------------------------------------------------
# Base image
# -------------------------------------------------
FROM python:3.10-slim

# -------------------------------------------------
# Environment settings
# -------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------------------------------
# System dependencies (required for Docling, FAISS)
# -------------------------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------------------------
# Set working directory
# -------------------------------------------------
WORKDIR /app

# -------------------------------------------------
# Install Python dependencies
# -------------------------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -------------------------------------------------
# Copy project files
# -------------------------------------------------
COPY . .

# -------------------------------------------------
# Expose FastAPI port
# -------------------------------------------------
EXPOSE 8000

# -------------------------------------------------
# Run FastAPI application
# -------------------------------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
``

