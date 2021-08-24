import datetime


class MoscowTime:
    hours: str
    minutes: str
    seconds: str

    def __init__(
        self, hours: str = "00", minutes: str = "00", seconds: str = "00"
    ):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def from_datetime(cls, timestamp: datetime.datetime) -> "MoscowTime":
        return cls(
            hours=str(timestamp.hour).zfill(2),
            minutes=str(timestamp.minute).zfill(2),
            seconds=str(timestamp.second).zfill(2),
        )

    @classmethod
    def from_timedelta(cls, delta: datetime.timedelta) -> "MoscowTime":
        return cls(
            hours=str(delta.seconds // 3600).zfill(2),
            minutes=str((delta.seconds // 60) % 60).zfill(2),
            seconds=str(delta.seconds % 60).zfill(2),
        )

    @classmethod
    def from_string(cls, s: str):
        return cls(*map(lambda s: s.zfill(2), s.split(":")))

    def to_timedelta(self) -> datetime.timedelta:
        return datetime.timedelta(
            hours=int(self.hours),
            minutes=int(self.minutes),
            seconds=int(self.seconds),
        )

    def __eq__(self, other: "MoscowTime") -> bool:
        return (
            self.hours == other.hours
            and self.minutes == other.minutes
            and self.seconds == other.seconds
        )

    def __add__(self, other: "MoscowTime") -> "MoscowTime":
        return MoscowTime.from_timedelta(
            self.to_timedelta() + other.to_timedelta()
        )

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    now = MoscowTime.from_string("11:13:5")
    interval = MoscowTime.from_string("25:23:10")
    print(interval)
    print(now + interval)
