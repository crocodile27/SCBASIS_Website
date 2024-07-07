# Use a newer Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /SCBASIS_rootdir

# Copy the current directory contents into the container at /SCBASIS_rootdir
ADD . /SCBASIS_rootdir

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
