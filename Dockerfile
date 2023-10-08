# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]
