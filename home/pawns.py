from itertools import product


def get_covering_positions(pawn: (int, int)) -> list:
    """
    Calculate positions that can cover given pawn.
    """
    hor, vert = pawn[0], pawn[1]
    covering_positions = []
    pos1 = (hor - 1, vert - 1)
    pos2 = (hor + 1, vert - 1)
    for pos in (pos1, pos2):
        if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            covering_positions.append(pos)
    return covering_positions


def safe_pawns(pawns: set) -> int:
    """
    Find pawns that are covered by at least 1 another pawn. Return the number of covered pawns.
    """
    covered_counter = 0
    pawns = [(ord(pawn[0]) - ord('a'), int(pawn[1])) for pawn in pawns]
    for pawn in pawns:
        covering_pos = get_covering_positions(pawn)
        if any(pos in pawns for pos in covering_pos):
            covered_counter += 1
    return covered_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
