# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all app files to the working directory
COPY . .

## Set Uploads Directory
#RUN mkdir -p /app/uploads

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Set the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]