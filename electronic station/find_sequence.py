from typing import List, Tuple
from itertools import product


def get_neighbour_deltas() -> List[Tuple[int, int]]:
    """ Return offsets to all neighbour cells """
    return [cell for cell in product(range(-1, 2), range(-1, 2)) if cell != (0, 0)]


def is_cell_in_matrix(matrix: List[List[int]], line: int, col: int) -> bool:
    """ Check if cell is in matrix or out of range """
    return all(val in range(len(matrix)) for val in (line, col))


def neighbour_matches(matrix: List[List[int]], line: int, col: int) -> Tuple[int, int]:
    """ Generator to find and yield all matching values among neighbouring cells """
    cell_value = matrix[line][col]
    matrix_size = len(matrix)
    for line_delta, col_delta in get_neighbour_deltas():
        check_line = line + line_delta
        check_col = col + col_delta
        if is_cell_in_matrix(matrix, check_line, check_col):
            check_cell_val = matrix[check_line][check_col]
            if check_cell_val == cell_value:
                yield line_delta, col_delta


def trace_sequence(matrix: List[List[int]], seq_len: int, start_line: int, start_col: int,
                   line_delta: int, col_delta: int) -> bool:
    """
    Recursive find sequence in matrix. Moves through matrix with given deltas and compares values.
    Return True if sequence length is 4 or more
    """
    check_line = start_line + line_delta
    check_col = start_col + col_delta
    if is_cell_in_matrix(matrix, check_line, check_col):
        if matrix[start_line][start_col] == matrix[check_line][check_col]:
            seq_len += 1
            if seq_len >= 4:
                return True
            else:
                return trace_sequence(matrix, seq_len, check_line, check_col, line_delta, col_delta)
    return False


def checkio(matrix: List[List[int]]) -> bool:
    """
    Check if there is a sequence of 4 matching digits in a matrix. Sequences
    can be located horizontally, vertically or diagonally
    """
    matrix_size = len(matrix)
    for line in range(matrix_size):
        for col in range(matrix_size):
            for match in neighbour_matches(matrix, line, col):
                if trace_sequence(matrix, seq_len=1, start_line=line, start_col=col,
                                  line_delta=match[0], col_delta=match[1]):
                    return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
