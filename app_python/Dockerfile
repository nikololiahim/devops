FROM python:3.6-slim-buster

LABEL author.name='Mikhail Olokin'
LABEL author.group='SE18-02'
LABEL author.email='m.olokin@innopolis.university'

WORKDIR app_python
COPY . .
RUN rm -rf venv && \
    apt-get update -y &&\
    apt-get upgrade -y &&\
    python3 -m pip install --upgrade pip &&\
    python3 -m pip install -r requirements/prod.txt &&\
    python3 -m pip install -e .

CMD [ "python3", "-m", "moscow_time.__init__"]
