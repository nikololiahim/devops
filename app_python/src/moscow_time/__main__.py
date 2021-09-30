import logging
import os

import waitress
from moscow_time import create_app

if __name__ == "__main__":
    app = create_app()
    DEBUG = os.getenv("PYTHON_APP_DEBUG", "on")
    if DEBUG == "on":
        app.logger.setLevel(logging.DEBUG)
    HOST = os.getenv("PYTHON_APP_HOST")
    PORT = os.getenv("PYTHON_APP_PORT")
    app.logger.info(
        f"""
    Application running at {HOST}:{PORT}
    Debug mode: {os.getenv("PYTHON_APP_DEBUG")}
    """
    )
    waitress.serve(app, host=HOST, port=PORT)
