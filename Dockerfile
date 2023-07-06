# Base image
FROM python:3.8.10

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Define the startup command
CMD ["gunicorn", "--workers", "4","--bind", "0.0.0.0:8080", "main:app"]
