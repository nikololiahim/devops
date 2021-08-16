from flask import Flask, render_template
import datetime
import pytz
from collections import namedtuple

app = Flask(__name__)
MoscowTime = namedtuple("MoscowTime", ["year", "month", "day", "hour", "minute", "second"])


@app.route('/')
def hello_world():
    msc_time = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_msc_time = MoscowTime(
        year=str(msc_time.year).zfill(2),
        month=str(msc_time.month).zfill(2),
        day=str(msc_time.day).zfill(2),
        hour=str(msc_time.hour).zfill(2),
        minute=str(msc_time.minute).zfill(2),
        second=str(msc_time.second).zfill(2),
    )
    return render_template("index.html",
                           date=formatted_msc_time)


if __name__ == '__main__':
    app.run()
