import logging

import waitress
from config import DEBUG, HOST, PORT

from app_python.src.moscow_time import create_app

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
