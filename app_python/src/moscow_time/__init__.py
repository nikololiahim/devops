import datetime
import logging
import os

import pytz
import waitress
from flask import Flask, render_template
from moscow_time.config import DEBUG, HOST, PORT
from moscow_time.models import MoscowTime

MOSCOW_TZ = pytz.timezone("Europe/Moscow")


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is not None:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello_world():
        msc_time = datetime.datetime.now(tz=MOSCOW_TZ)
        app.logger.debug(f"CURRENT TIME IN MOSCOW: {msc_time}")
        return render_template(
            "index.html", date=MoscowTime.from_datetime(msc_time)
        )

    return app


if __name__ == "__main__":
    app = create_app()
    if DEBUG:
        app.logger.setLevel(logging.DEBUG)
    app.logger.info(
        f"""
    Application running at {HOST}:{PORT}
    Debug mode: {"on" if DEBUG else "off"}
    """
    )
    waitress.serve(app, host=HOST, port=PORT)
