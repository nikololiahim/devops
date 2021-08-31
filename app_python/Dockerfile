FROM python:3.6-slim-buster

LABEL author.name='Mikhail Olokin'
LABEL author.group='SE18-02'
LABEL author.email='m.olokin@innopolis.university'

WORKDIR app_python
COPY . .
RUN python3 -m pip install --upgrade pip pipenv &&\
    pipenv install --deploy --dev

CMD [ "python3", "-m", "moscow_time.__init__"]
