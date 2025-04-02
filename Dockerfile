# Use the official lightweight Python image.
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Set the port that Cloud Run will use
ENV PORT 8080

# Command to run the app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]