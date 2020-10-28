# Set the base image
FROM python:3.9

# File Author / Maintainer
MAINTAINER bjg

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Copy the application folder inside the container
ADD /app_files /app_files

# Get pip to download and install requirements:
RUN pip install -r /app_files/requirements.txt

# Expose listener port
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /app_files
RUN mkdir /data
# Set the default command to execute    
# when creating a new container
CMD python flaskApp.py
