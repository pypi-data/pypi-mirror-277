from datetime import datetime


def toTimestamp(date: datetime, offset_second: int):
    return (date.timestamp() + offset_second) * 1000


def parseDate(text: str):
    f_text = str.join(" ", text.split()[2:])
    return datetime.strptime(f_text, "%b %d %I:%M:%S %Y")


__all__ = ["toTimestamp", "parseDate"]
