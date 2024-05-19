# Use the Python image 
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code to the working directory
COPY app /app

# Specify the command to run the FastAPI application
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","8000"]