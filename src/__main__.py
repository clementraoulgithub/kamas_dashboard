from apscheduler.schedulers.background import BackgroundScheduler

from src.controllers.app import app
from src.utils.scraping import get_current_kamas_value

scheduler = BackgroundScheduler()

if __name__ == "__main__":
    for server in ["boune", "crail", "eratz", "galgarion", "henual"]:
        scheduler.add_job(
            lambda server=server: get_current_kamas_value(server), "interval", hours=0.1
        )
    scheduler.start()
    app.run_server(debug=True, use_reloader=True)
