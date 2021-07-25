from datetime import datetime


def format_day(dt: datetime) -> str:
    """
    Format year, month and day in readable format
    """
    month = datetime.strftime(dt, '%B')
    return f'{dt.day} {month} {dt.year} year'


def format_time(dt: datetime) -> str:
    """format hours and minustes in readabale format"""
    h, m = dt.hour, dt.minute
    h_formatted = f'{h} hour' if h == 1 else f'{h} hours'
    m_formatted = f'{m} minute' if m == 1 else f'{m} minutes'
    return h_formatted + ' ' + m_formatted


def date_time(time: str) -> str:
    """
    Convert date and time into readable format. For example:
    "01.01.2000 00:00" -> "1 January 2000 year 0 hours 0 minutes"
    """
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    return format_day(dt) + ' ' + format_time(dt)


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
