import time


def formatted_time(hour: str, minute: str, second: str) -> bytes:
    return f"Time: {hour}:{minute}:{second}".encode()


def test_correct_timezone(response):
    assert "Moscow, Russian Federation".encode() in response


def test_correct_time(response, now):
    assert (
        formatted_time(now["hour"], now["minute"], now["second"]) in response
    )


def test_correct_time_on_update(client, now):
    response = client.get("/").data
    before = now
    assert (
        formatted_time(before["hour"], before["minute"], before["second"])
        in response
    )
    time.sleep(1)
    response = client.get("/").data
    seconds_after = str(int(before["second"]) + 1).zfill(2)
    assert (
        formatted_time(before["hour"], before["minute"], seconds_after)
        in response
    )
