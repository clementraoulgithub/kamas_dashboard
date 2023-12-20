from apscheduler.schedulers.background import BackgroundScheduler
import os
from src.controllers.app import app
from src.utils.scraping import get_current_kamas_value

scheduler = BackgroundScheduler()

if __name__ == "__main__":
    for server in ["boune", "crail", "eratz", "galgarion", "henual"]:
        scheduler.add_job(
            lambda server=server: get_current_kamas_value(server), "interval", hours=1
        )
    scheduler.start()
    
    debug = os.environ.get("BACKEND_HOST", "localhost") == "localhost"
    app.run_server(debug=debug, host="0.0.0.0", port=80)
