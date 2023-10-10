# Single Dockerfile for all tasks
FROM python:3.8
COPY . /app/
WORKDIR /app
RUN pip install pika

#docker-compose up neegit ds to be run from root dir