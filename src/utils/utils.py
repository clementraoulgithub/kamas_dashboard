import datetime
import logging
from logging.handlers import RotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
import tzlocal

from src.utils.scraping import get_current_kamas_value

def schedule_scrapping():
    scheduler = BackgroundScheduler()

    for server in ["boune", "crail", "eratz", "galgarion", "henual"]:
        scheduler.add_job(
            get_current_kamas_value,
            "interval",
            args=[server],
            minutes=10,
        )
    print("Start the scheduler")
    scheduler.start()

def get_offset_time_zone() -> datetime.timedelta | None:
    """
    Get the offset of the local timezone

    Returns:
        datetime.timedelta | None: the offset of the local timezone
    """
    local_timezone = pytz.timezone(str(tzlocal.get_localzone()))
    local_time = datetime.datetime.now(local_timezone)
    return local_time.utcoffset()


def logger_config(level: int = logging.INFO) -> None:
    """
    Configure the logger

    Args:
        level (str): level of the logger

    Returns:
        logging.Logger: the configured logger
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch = logging.StreamHandler()
    fh = RotatingFileHandler("logs.log", maxBytes=10_000_000, backupCount=5)

    for handler in (ch, fh):
        handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
