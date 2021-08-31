"""
From a set of ints you have to create a list of closed intervals as tuples,
so the intervals are covering all the values found in the set.
Input: A set of ints.
Output: A list of tuples of two ints, indicating the endpoints of the interval.
The Array should be sorted by start point of each interval
https://py.checkio.org/mission/create-intervals/solve/
"""
from typing import List, Tuple


def create_intervals(data: set) -> List[Tuple]:
    """ Create a list of intervals out of set of ints. """
    data = sorted(data)
    interval_begin, interval_end = None, None
    intervals = []
    for num in data:
        if interval_begin is None:
            interval_begin = num
        if interval_end is None:
            interval_end = num
        else:
            if num - interval_end > 1:
                intervals.append((interval_begin, interval_end))
                interval_begin = num
                interval_end = num
            else:
                interval_end = num
    if interval_begin is not None and interval_end is not None:
        intervals.append((interval_begin, interval_end))
    return intervals


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals(set()) == []
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
