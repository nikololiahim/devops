import datetime
from typing import Optional

import freezegun
import pytest


def formatted_time(time: dict) -> bytes:
    return f"Time: {time['hour']}:{time['minute']}:{time['second']}".encode()


def inc_time(
    time: dict,
    hours: Optional[int] = None,
    minutes: Optional[int] = None,
    seconds: Optional[int] = None,
) -> dict:
    time = time.copy()
    for value, attr in (
            (hours, "hour"),
            (minutes, "minute"),
            (seconds, "second"),
    ):
        if value is not None:
            time[attr] = str(int(time[attr]) + value).zfill(2)
    return time


def test_correct_timezone(response):
    assert "Moscow, Russian Federation".encode() in response


def test_correct_time(response, now):
    assert formatted_time(now) in response


@pytest.mark.parametrize(
    "interval",
    [
        {"seconds": 3},
        {"minutes": 3},
        {"hours": 3},
        {"hours": 3, "seconds": 3},
        {"hours": 3, "minutes": 3},
        {"minutes": 3, "seconds": 3},
        {"hours": 3, "minutes": 3, "seconds": 3},
    ],
)
def test_correct_time_on_update(client, now_as_timestamp, now, interval):
    response = client.get("/").data
    before = now
    assert formatted_time(before) in response

    # some time later...
    with freezegun.freeze_time(now_as_timestamp) as frozen_time:
        frozen_time.tick(delta=datetime.timedelta(**interval))
        response = client.get("/").data
        after = inc_time(before, **interval)
        assert formatted_time(after) in response
