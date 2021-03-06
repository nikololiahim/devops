import datetime
import os

import psycopg2
import pytz
from flask import Flask, render_template, request
from moscow_time.models import MoscowTime

MOSCOW_TZ = pytz.timezone("Europe/Moscow")


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("APP_PYTHON_SECRET_KEY", "dev")
    )
    conn = psycopg2.connect(
        dbname="postgres",
        host="postgres",
        user="postgres",
        password="postgres",
    )
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS visits (
            timestamp_ timestamptz NOT NULL,
            host varchar(50) NOT NULL,
            PRIMARY KEY (timestamp_)
            )""".strip()
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
        msc_time = datetime.datetime.now(tz=MOSCOW_TZ)
        app.logger.debug(f"CURRENT TIME IN MOSCOW: {msc_time}")
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO visits (timestamp_, host) VALUES (%s, %s)
                """.strip(),
                (msc_time, dict(request.headers).get("Host")),
            )
        return render_template(
            "index.html", date=MoscowTime.from_datetime(msc_time)
        )

    @app.route("/visits")
    def visits():
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM visits
                ORDER BY timestamp_
                """
            )
            rows = cur.fetchall()
            return render_template("visits.html", data=rows, total=len(rows))

    return app
