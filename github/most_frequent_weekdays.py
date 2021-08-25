"""
You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year. The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
Input: Year as an int .
Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).
Preconditions: Year is between 1 and 9999. Week starts with Monday.
https://py.checkio.org/mission/the-most-frequent-weekdays/solve/
"""

import datetime
from typing import List

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year: int) -> List[str]:
    """ Determine the most frequent weekday in a given year """
    first_day = datetime.datetime(year, 1, 1)
    first_weekday = first_day.weekday()
    first_day_of_next = datetime.datetime(year + 1, 1, 1)
    delta = (first_day_of_next - first_day).days
    day_shift = delta % 7
    result = [weekdays[(first_weekday + x) % 7] for x in range(day_shift)]
    return sorted(result, key=lambda x: weekdays.index(x))


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
