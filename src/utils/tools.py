"""Utils functions"""

import datetime
import logging
from enum import Enum, unique
from logging.handlers import RotatingFileHandler

import pytz
import tzlocal


@unique
class Server(Enum):
    """Enum of the differents servers"""

    BOUNE = "boune"
    CRAIL = "crail"
    ERATZ = "eratz"
    GALGARION = "galgarion"
    HENUAL = "henual"


@unique
class LineGraphScope(Enum):
    """Enum of the differents line graph scope"""

    YEAR = 0
    SIX_MONTHS = 1
    THREE_MONTHS = 2
    MONTH = 3
    WEEK = 4
    DAY = 5


@unique
class Website(Enum):
    D2GATE = ("D2gate", "https://fr.d2gate.net")
    KAMAS_FACILE = ("Kamas facile", "https://www.kamasfacile.com")
    FUN_SHOP = ("Fun shop", "https://www.funshopes.com")
    MODE_MARCHAND = ("Mode marchand", "https://www.mode-marchand.net")
    TRY_AND_JUDGE = ("Try and judge", "https://www.tryandjudge.com")
    IG_PLAYS = ("Ig plays", "https://www.igplays.com")
    LEKAMAS = ("Le kamas", "https://www.lekamas.fr/")


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
