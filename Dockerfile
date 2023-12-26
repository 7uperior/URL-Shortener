# Use Python 3.10 as the base image
FROM python:3.10

RUN mkdir /URL-Shortener
RUN mkdir /URL-Shortener/url-shortener/

COPY /url-shortener /URL-Shortener/url-shortener/
COPY pyproject.toml /URL-Shortener
COPY .env /URL-Shortener

WORKDIR /URL-Shortener
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 


RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev