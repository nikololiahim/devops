import freezegun
import pytest

from moscow_time.models import MoscowTime


def formatted_time(time: "MoscowTime") -> bytes:
    return str(time).encode()


def test_correct_timezone(response):
    assert "Moscow, Russian Federation".encode() in response


def test_correct_time(response, now):
    assert formatted_time(now) in response


@pytest.mark.parametrize(
    "interval",
    [
        MoscowTime(seconds="03"),
        MoscowTime(minutes="03"),
        MoscowTime(hours="03"),
        MoscowTime(hours="03", seconds="03"),
        MoscowTime(hours="03", minutes="03"),
        MoscowTime(minutes="03", seconds="03"),
        MoscowTime(hours="03", minutes="03", seconds="03"),
    ],
)
def test_correct_time_on_update(client, now_as_timestamp, now, interval):
    response = client.get("/").data
    before = now
    assert formatted_time(before) in response

    # some time later...
    with freezegun.freeze_time(now_as_timestamp) as frozen_time:
        frozen_time.tick(delta=interval.to_timedelta())
        response = client.get("/").data
        after = before + interval
        assert formatted_time(after) in response


@pytest.mark.parametrize(
    "start,inc,expected",
    [
        (
            MoscowTime(hours="11", minutes="59", seconds="59"),
            MoscowTime(seconds="01"),
            MoscowTime(hours="12"),
        ),
        (
            MoscowTime(hours="11", minutes="58", seconds="59"),
            MoscowTime(minutes="01", seconds="01"),
            MoscowTime(hours="12"),
        ),
    ],
)
def test_inc_time(start, inc, expected):
    assert start + inc == expected
