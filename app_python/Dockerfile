FROM python:3.9.7-slim-buster

LABEL author.name='Mikhail Olokin'
LABEL author.group='SE18-02'
LABEL author.email='m.olokin@innopolis.university'

ENV PYTHON_APP_HOST 0.0.0.0
ENV PYTHON_APP_PORT 8000
ENV PYTHON_APP_DEBUG on

WORKDIR app_python
COPY . .
RUN apt-get -y update &&\
    apt-get -y install libpq-dev gcc &&\
    python3 -m pip install --upgrade pip pipenv &&\
    pipenv install --deploy --dev
