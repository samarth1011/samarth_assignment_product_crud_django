# Pulls Python 3 image from docker hub
FROM python:3

# Used when running python in docker container ensures logs are outputted in console
ENV PYTHONUNBUFFERED 1
RUN mkdir /assignment
WORKDIR /assignment
COPY . /assignment/
RUN pip install -r requirements.txt