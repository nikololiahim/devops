# Python Best Practices Used

- [virtual environments](https://docs.python.org/3/library/venv.html) for reproducible and platform-independent builds

- 'src-layout' and application packaging
  (more about this [here](https://docs.pytest.org/en/6.2.x/goodpractices.html) and
  particularly [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure))

- [pyproject.toml](https://www.python.org/dev/peps/pep-0518/#specification) - one place for all (mostly) your tool
  configs

- using
  [conftest.py](https://docs.pytest.org/en/6.2.x/fixture.html?highlight=conftest#conftest-py-sharing-fixtures-across-multiple-files)
  to define fixtures (Pytest specific)
- mocking `datetime` module in unit tests using `freezegun` library to avoid waiting a long time and time-related issues

- [pipenv](https://pipenv.pypa.io/en/latest/) to install and manage dependencies
- [.gitignore template](https://github.com/github/gitignore/blob/master/Python.gitignore) provided by Github
- config.py file for storing application configurations
- configurable [logging](https://flask.palletsprojects.com/en/2.0.x/logging/) built into Flask object
- [pre-commit](https://pre-commit.com/) hooks to run the formatting tools automatically

# Frameworks/Libraries Used

- [flask](https://github.com/pallets/flask) - a popular Python web-framework with minimum boilerplate that can also be
  used in industry-scale web applications
- [pytz](https://github.com/stub42/pytz/blob/master/src/README.rst) - a library used for time calculations, in
  particular, for making sure that we are indeed using the Moscow time
- [pytest](https://github.com/pytest-dev/pytest) - a de-facto industry standard framework for writing and running tests
- [freezegun](https://github.com/spulec/freezegun) - a mocking framework designed specifically to mock time-related
  actions
- [waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/) - a production-ready WSGI server
  implementation

# Tools Used
All these tools
- [flake8](https://github.com/PyCQA/flake8) - an aggregate of several Python linters
- [black](https://github.com/psf/black) - a widely used code formatter
- [isort](https://github.com/PyCQA/isort) - a tool to sort imports in alphabetic order
- Python/Markdown linters and formatters built into [Pycharm](https://www.jetbrains.com/pycharm/)
