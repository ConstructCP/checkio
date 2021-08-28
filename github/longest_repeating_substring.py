"""
Find the first longest repeating sequence inside the string.
Example: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"
Input: String.
Output: String.
https://py.checkio.org/mission/long-repeat-inside/solve/
"""
from collections import Counter
from contextlib import suppress
from typing import List, Dict, Tuple, Iterable


def count_all_substrings(s: str) -> Counter:
    """ Count all substrings in string """
    counter = Counter()
    for i, char in enumerate(s):
        for j in range(i + 1):
            substr = s[i - j: i + 1]
            if len(set(substr)) == len(substr):
                counter[substr] = counter.get(substr, 0) + 1
    return counter


def find_longest(strings: Iterable) -> List[str]:
    max_len = max(map(len, strings))
    return [s for s in strings if len(s) == max_len]


def find_the_first_substr(string: str, substrings: List[str]) -> str:
    """
    Get the first substring found in string. In case if several substring start
    from the same position - pick the longest
    """
    first_indexes = {s: string.index(s) for s in substrings}
    first_indexes_sorted = sorted(first_indexes.items(), key=lambda x: x[1])
    return first_indexes_sorted[0][0]


def extract_all_substrings(substring: str, string: str) -> str:
    """ Extract all occurencies of substring in string """
    substr_indexes = []
    search_start = 0
    try:
        for i in range(len(string)):
            substr_beg = string.index(substring, search_start)
            substr_indexes.append((substr_beg, substr_beg + len(substring) - 1))
            search_start = substr_beg + 1
    except ValueError:
        pass
    substr_indexes = merge_intervals(substr_indexes)
    substr_indexes = sorted(substr_indexes, key=lambda i: i[1] - i[0], reverse=True)
    longest_interval = substr_indexes[0]
    return ''.join([string[i] for i in range(longest_interval[0], longest_interval[1] + 1)])


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """ Get all numbers that are located within given intervals """
    if len(intervals) == 1:
        return intervals
    merged_intervals = []
    int_beg, int_end = None, None
    for int in intervals:
        if int_beg is None and int_end is None:
            int_beg = int[0]
            int_end = int[1]
            continue
        if int_end > int[0] or int_end + 1 == int[0]:
            int_end = int[1]
        else:
            merged_intervals.append((int_beg, int_end))
            int_beg = int[0]
            int_end = int[1]
    merged_intervals.append((int_beg, int_end))
    return merged_intervals


def repeat_inside(line: str) -> str:
    """ Find the first longest repeating substring """
    substring_count = count_all_substrings(line)
    substring_count = {k: v for k, v in substring_count.items() if v > 1}
    if not substring_count:
        return ''
    longest_substrings = find_longest(substring_count.keys())
    if len(longest_substrings) == 1:
        return extract_all_substrings(longest_substrings[0], line)
    else:
        first_longest = find_the_first_substr(line, longest_substrings)
        return extract_all_substrings(first_longest, line)


if __name__ == '__main__':
    print(
        repeat_inside("rghtyjdfrtdfdf56r")
    )
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
