"""Entry point of the application."""

import os

from src.utils.scraping import schedule_scrapping

schedule_scrapping()
debug = os.environ.get("BACKEND_HOST", "localhost") == "localhost"

# pylint: disable=wrong-import-position
# pylint: disable=unused-import
from src.app import app, server

if __name__ == "__main__":
    app.run(debug=debug, host="0.0.0.0", port=80)
