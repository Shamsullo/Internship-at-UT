FROM python:3

MAINTAINER Shams

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY dependencies.txt /code/
RUN pip install -r dependencies.txt
COPY . /code/
