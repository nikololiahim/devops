import datetime
import os
from collections import namedtuple

import pytz
from flask import Flask, render_template

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
        app.logger.debug(f"CURRENT TIME IN MOSCOW: {msc_time}")
        formatted_msc_time = MoscowTime(
            hour=zfill(msc_time.hour),
            minute=zfill(msc_time.minute),
            second=zfill(msc_time.second),
        )
        return render_template("index.html", date=formatted_msc_time)

    return app
