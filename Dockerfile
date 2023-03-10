FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install
RUN ls -la
COPY . /app/
