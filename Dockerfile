# Use a newer Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /SCBASIS_rootdir

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /SCBASIS_rootdir/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /SCBASIS_rootdir/

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
