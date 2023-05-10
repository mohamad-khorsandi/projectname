# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set environment variables for Django (optional)
ENV DJANGO_SETTINGS_MODULE=myapp.settings
ENV PYTHONUNBUFFERED=1

# Start the Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]