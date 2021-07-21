from itertools import product


def safe_pawns(pawns: set) -> int:
    hor_grid = list('abcdefgh')
    covered_counter = 0
    pawns = [(pawn[0], int(pawn[1])) for pawn in pawns]
    print(pawns)
    for pawn in pawns:
        hor = pawn[0]
        vert = pawn[1]

        if vert == 1:
            continue
        if hor == 'a':
            covering_positions = (('b', vert - 1),)
        elif hor == 'h':
            covering_positions = (('g', vert - 1),)
        else:
            hor_index = hor_grid.index(hor)
            covering_positions = (
                (hor_grid[hor_index - 1], vert - 1),
                (hor_grid[hor_index + 1], vert - 1)
            )

        if any(pos in pawns for pos in covering_positions):
            covered_counter += 1
    return covered_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
