"""
Determine the number of operations from this list required to paint the designated length of the wall.
If it's impossible to paint that length with the given operations, then return -1.
Input: Two arguments.
    The required length of the wall that should be painted, as integer.
    A list of the operations that contains the range (inclusive) as a list of two integers.
Output: The minimum number of operations. If you cannot paint enough of the length with the given operations, return -1.
https://py.checkio.org/mission/painting-wall/solve/
"""
from typing import List


def checkio(required: int, operations: List[List[int]]) -> int:
    """ Return the number of operation required to cover given required length of the wall """
    operations_performed = 0
    already_painted = []
    for operation in operations:
        if is_already_covered(already_painted, operation):
            operations_performed += 1
            continue
        # already_painted = recalculate_coverage(already_painted, operation)
        already_painted.append(operation)
        already_painted = merge_intervals(already_painted)
        operations_performed += 1
        if sum_coverage(already_painted) >= required:
            break
    else:
        return -1
    return operations_performed


def is_already_covered(coverage: List[List[int]], operation: List[int]) -> bool:
    """ Determine whether operation overlaps already covered interval """
    for interval in coverage:
        if interval[0] < operation[0] and operation[1] < interval[1]:
            return True
    return False


def recalculate_coverage(coverage: List[List[int]], operation: List[int]) -> List[List[int]]:
    """ Recalculate coverage after operation peformed """
    new_coverage = []
    for interval in coverage:
        if interval[1] < operation[0] or interval[0] > operation[1]:
            new_coverage.append(interval)
        else:
            beg = min(interval[0], operation[0])
            end = max(interval[1], operation[1])
            new_coverage.append([beg, end])

    merged_coverage = merge_intervals(new_coverage)
    return merged_coverage


def sum_coverage(coverage: List[List[int]]) -> int:
    """ Get total number of tiles covered """
    total = sum(interval[1] - interval[0] + 1 for interval in coverage)
    return total


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """ Unite overlapping intervals in list """
    if len(intervals) == 1:
        return intervals
    intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = []
    int_beg, int_end = None, None
    for i in intervals:
        if int_beg is None and int_end is None:
            int_beg = i[0]
            int_end = i[1]
            continue
        if int_end > i[0] or int_end + 1 == i[0]:
            int_end = max(i[1], int_end)
        else:
            merged_intervals.append([int_beg, int_end])
            int_beg = i[0]
            int_end = i[1]
    merged_intervals.append([int_beg, int_end])
    return merged_intervals


if __name__ == '__main__':
    print(
        checkio(30, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]])
    )

    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"