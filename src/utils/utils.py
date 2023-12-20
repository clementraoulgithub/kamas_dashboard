import datetime

import pytz
import tzlocal


def get_offset_time_zone() -> datetime.timedelta | None:
    """
    Get the offset of the local timezone

    Returns:
        datetime.timedelta | None: the offset of the local timezone
    """
    local_timezone = pytz.timezone(str(tzlocal.get_localzone()))
    local_time = datetime.datetime.now(local_timezone)
    return local_time.utcoffset()

