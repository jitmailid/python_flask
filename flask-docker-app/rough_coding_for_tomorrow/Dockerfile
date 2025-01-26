# Use the official Python image as the base image
FROM python:3.10-slim

# Set a working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5001

# Run the application
CMD ["python", "helloflask.py"]
