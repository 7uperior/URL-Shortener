# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in pyproject.toml
RUN pip install poetry
RUN poetry install

# Run main.py when the container launches
CMD ["python", "./url-shortener/main.py"]
