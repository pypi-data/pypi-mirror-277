from datetime import datetime


def to_timestamp(date: datetime, offset_second: int) -> int:
    """Converts a datetime object to a timestamp in milliseconds with an offset."""
    return int((date.timestamp() + offset_second) * 1000)


def parse_date(text: str) -> datetime:
    """Parses a string to a datetime object."""
    f_text = " ".join(text.split()[2:])
    return datetime.strptime(f_text, "%b %d %I:%M:%S %Y")


__all__ = ["to_timestamp", "parse_date"]
