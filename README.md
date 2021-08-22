# moscow_time

A simple web app that displays current time in Moscow, Russian Federation

## Getting Started

In order to install the project you need to have Python 3.6+ installed in your system. For some systems (Ubuntu), you
also need to install `pip` and `venv`:

```
sudo apt install -y python3-pip
sudo apt install -y python3-venv
```

### Dependencies

* flask
* pytz
* waitress

### Development-specific dependencies

* pytest-flask
* black
* flake8
* freezegun

### Installing

```bash 
   git clone https://github.com/nikololiahim/devops
   cd app_python
   python3 -m pip install -r requirements.txt
   python3 -m pip install -e .
```

### Executing program

```
    python3 -m moscow_time.__init__
```

## Docker

This app can be run as a Docker container. The image is
available [on Dockerhub](https://hub.docker.com/repository/docker/nikololiahim/moscow_time).

## Configuration

An app is configurable through `config.py` file. Some available options are:

* `DEBUG` - whether to display debug messages or not
* `PORT` - the port to run application at
* `HOST` - IP address of the host to run the application at

## Authors

| Name           | E-mail                        | Github        |
|----------------|-------------------------------|---------------|
| Mikhail Olokin | m.olokin@innopolis.university | @nikololiahim |

## Version History

* 0.0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements

I used [this](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc) template for this `README.md`
structure
