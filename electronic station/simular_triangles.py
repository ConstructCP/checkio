from typing import List, Tuple

Coords = List[Tuple[int, int]]
from math import sqrt
from itertools import combinations


def side_length(apex1: Tuple[int, int], apex2: Tuple[int, int]) -> float:
    """
    Calculate length of triangle side.
    """
    return sqrt((apex1[0] - apex2[0]) ** 2 + (apex1[1] - apex2[1]) ** 2)


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    """Check geometrical simularity of two triangles"""
    sides_1 = sorted([side_length(apex1, apex2)
                      for apex1, apex2 in combinations(coords_1, r=2)])
    sides_2 = sorted([side_length(apex1, apex2)
                      for apex1, apex2 in combinations(coords_2, r=2)])

    sides_ratio = [side_from_1 / side_from_2
                   for side_from_1, side_from_2 in zip(sides_1, sides_2)]
    return len(set(sides_ratio)) == 1


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
