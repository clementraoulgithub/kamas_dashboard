from apscheduler.schedulers.background import BackgroundScheduler

from src.controllers.app import app
from src.utils.scraping import get_current_kamas_value

scheduler = BackgroundScheduler()

if __name__ == "__main__":
    scheduler.add_job(get_current_kamas_value, "interval", hours=0.1)
    scheduler.start()
    app.run_server(debug=True)
