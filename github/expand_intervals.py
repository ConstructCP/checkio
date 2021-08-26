"""
Given an an iterable with intervals, create and return the list that contains all the integers contained by these intervals.
Input: The iterable of tuples of two integers.
Output: The iterable of integers.
Precondition: Each element in the interval is an integer and
https://py.checkio.org/mission/expand-intervals/solve/
"""

from typing import Iterable


def expand_intervals(items: Iterable) -> Iterable:
    """ Get ints that are contained in given collection of intervals """
    numbers = []
    for beg, end in items:
        in_interval = [i for i in range(beg, end + 1)]
        numbers.extend(in_interval)
    return numbers


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")
