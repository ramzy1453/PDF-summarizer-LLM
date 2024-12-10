FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV GOOGLE_API_KEY=AIzaSyBQYrjkbWyJeKguOMlwwXUM-LF9nX_sqxs

# Run app.py when the container launches
CMD ["python", "app.py"]