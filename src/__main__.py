"""Entry point of the application."""

from src.utils.scraping import schedule_scrapping

schedule_scrapping()

from src.app import app, server

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
