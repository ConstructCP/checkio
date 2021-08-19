from typing import List, Tuple, Union


def winning_sequences() -> List[Tuple[int, int]]:
    """ Generate sequences where all characters must be the same for win """
    for i in range(3):
        yield [(i, j) for j in range(3)]
        yield [(j, i) for j in range(3)]
    yield [(0, 0), (1, 1), (2, 2)]
    yield [(0, 2), (1, 1), (2, 0)]


def is_win(game_result: List[str], seq: List[Tuple[int, int]]) -> Union[str, None]:
    """ Check if given sequence in the game field consists equal symbols"""
    seq_symbols = [game_result[cell[0]][cell[1]] for cell in seq]
    if len(set(seq_symbols)) == 1:
        if seq_symbols[0] in 'XO':
            return seq_symbols[0]
    return None


def checkio(game_result: List[str]) -> str:
    """ Gets Xs and Os game field and determines the winner. Returns winning symbol or 'D' in case of draw. """
    for seq in winning_sequences():
        if res := is_win(game_result, seq):
            return res
    return 'D'



if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
