import os
from flask import Flask, render_template
import datetime
import pytz
from collections import namedtuple

MoscowTime = namedtuple("MoscowTime", ["hour", "minute", "second"])


def zfill(num: int) -> str:
    return str(num).zfill(2)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello_world():
        msc_time = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
        formatted_msc_time = MoscowTime(
            hour=zfill(msc_time.hour),
            minute=zfill(msc_time.minute),
            second=zfill(msc_time.second),
        )
        return render_template("index.html", date=formatted_msc_time)

    return app
