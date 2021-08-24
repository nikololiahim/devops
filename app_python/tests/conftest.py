import datetime

import pytest
from moscow_time import MOSCOW_TZ, create_app
from moscow_time.models import MoscowTime


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def now_as_timestamp():
    yield datetime.datetime.now(tz=MOSCOW_TZ)


@pytest.fixture
def response(client):
    yield client.get("/").data


@pytest.fixture
def now():
    current_time = datetime.datetime.now(tz=MOSCOW_TZ)
    yield MoscowTime.from_datetime(current_time)
