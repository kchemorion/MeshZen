# Set the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --index-url=http://localhost:3141/root/pypi/+simple/ --trusted-host=localhost -r requirements.txt

# Copy the project files
COPY . .

# Set environment variables
ENV DEBUG=True
ENV SECRET_KEY=your_secret_key_here
ENV DATABASE_URL=postgres://user:password@db:5432/meshzen_db

# Expose the port
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
