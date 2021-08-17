import datetime

import pytest
import pytz

from moscow_time import create_app, zfill


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def response(client):
    yield client.get("/").data


@pytest.fixture
def now():
    current_time = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    yield {
        "hour": zfill(current_time.hour),
        "minute": zfill(current_time.minute),
        "second": zfill(current_time.second),
    }
