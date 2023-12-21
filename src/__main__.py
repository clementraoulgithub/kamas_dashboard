from apscheduler.schedulers.background import BackgroundScheduler

from src.utils.scraping import get_current_kamas_value
from src.utils.utils import logger_config

scheduler = BackgroundScheduler()

for server in ["boune", "crail", "eratz", "galgarion", "henual"]:
    scheduler.add_job(
        get_current_kamas_value,
        "interval",
        args=[server],
        minutes=10,
    )
scheduler.start()

from src.controllers.app import app, server

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
