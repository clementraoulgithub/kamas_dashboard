
from src.utils.scraping import get_current_kamas_value
from src.utils.utils import logger_config, schedule_scrapping


schedule_scrapping()

from src.controllers.app import app, server

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
