# Use the official Python image as the base image
FROM python:3.11.6

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /splitwise_be_clone

# Copy the requirements file and install dependencies
COPY ./requirements.txt /splitwise_be_clone/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get autoremove -y
RUN apt-get autoclean -y
RUN apt-get clean -y

COPY . .
