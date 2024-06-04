from datetime import datetime
import pytz
import tzlocal  # This library helps to get the system's local timezone


def old_get_dt(include_tz: bool = False, as_str: bool = False) -> str | datetime:
    # todo note: timezone 포함시 datetime.timezone 객체임에 주의
    dt = datetime.now()
    if include_tz:
        dt = dt.astimezone()
    if as_str:
        if include_tz:
            dt = dt.strftime("%Y%m%d_%H%M%S%Z")
        else:
            dt = dt.strftime("%Y%m%d_%H%M%S")
    return dt


def get_dt(include_tz: bool = False, as_str: bool = False) -> str | datetime:
    # todo note: timezone 포함시 zoneinfo.ZoneInfo 객체임에 주의!
    local_timezone = tzlocal.get_localzone()  # <-- local system timezone
    dt = datetime.now()
    if include_tz:
        dt = datetime.now(local_timezone)
    if as_str:
        if include_tz:
            dt = dt.strftime("%Y%m%d_%H%M%S%Z")
        else:
            dt = dt.strftime("%Y%m%d_%H%M%S")
    return dt
