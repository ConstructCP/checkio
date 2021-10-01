"""
The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented
by lists of two numbers.
Input: A list of lines as a list of list. Each list consists of the two integers.
Output: The quantity of squares formed as an integer.
https://py.checkio.org/mission/the-square-chest
"""


from typing import List, Dict

GRID_SIZE = 4


def try_draw_square(connections: Dict[int, List], top_left: int, side_len: int) -> bool:
    """ Check if we can draw square starting at given top_left point with given side_len """
    if top_left % GRID_SIZE + side_len > GRID_SIZE:
        return False
    top_right = top_left + side_len
    bottom_left = top_left + GRID_SIZE * side_len
    horizontal_side_step = 1
    vertical_side_step = GRID_SIZE
    if (try_draw_side(connections, top_left, side_len, horizontal_side_step)
        and try_draw_side(connections, top_left, side_len, vertical_side_step)
        and try_draw_side(connections, top_right, side_len, vertical_side_step)
        and try_draw_side(connections, bottom_left, side_len, horizontal_side_step)
    ):
        return True
    else:
        return False


def try_draw_side(connections: Dict[int, List], start_point: int, side_len: int, step: int) -> bool:
    """
    Check if we can draw side of a square from given start_point with given side len.
    Step represents how many points to skip to get the next point of square side
    """
    prev_point = start_point
    for i in range(1, side_len + 1):
        current_point = start_point + step * i
        if current_point not in connections[prev_point]:
            return False
        prev_point = current_point
    return True


def represent_as_connections_graph(lines_list: List[List[int]]) -> Dict[int, List]:
    """ Convert list of lines to graph representation with dict {points: lists_of_connected} """
    connections = {x: list() for x in range(GRID_SIZE ** 2)}
    for line in lines_list:
        point1, point2 = line[0] - 1, line[1] - 1
        connections[point1].append(point2)
        connections[point2].append(point1)
    return connections


def checkio(lines_list: List[List[int]]) -> int:
    """ Return the quantity of squares """
    connections = represent_as_connections_graph(lines_list)
    squares_number = 0
    for point in range(GRID_SIZE * (GRID_SIZE - 1)):
        for square_side in range(1, GRID_SIZE + 1):
            if try_draw_square(connections, point, square_side):
                squares_number += 1
    return squares_number


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")
