FROM python:3

LABEL "author"="Varun"
LABEL "maintainer"="Varun"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
