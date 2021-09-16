from typing import List


def sum_rows(rows: List[str]) -> str:
    """
    Sum the list of rows. If symbol in some position is the same for all rows - put that symbol in its position,
    otherwise put '?'
    """
    resulting_row = ''
    for values in zip(*rows):
        reduced_symbol = set(values)
        if len(reduced_symbol) == 1:
            resulting_row += reduced_symbol.pop()
        else:
            resulting_row += '?'
    return resulting_row


def is_matches(row: str, proposed_fill: str) -> bool:
    """ Check if row matches the proposed fill. '?' can match any symbol, 'X' and 'O' can match only themselves. """
    for r1, r2 in zip(row, proposed_fill):
        if r2 == '?':
            continue
        else:
            if r1 != r2:
                return False
    return True


def generate_rows(row_len: int, filled_sequences_lengths: List[int]) -> List[str]:
    """
    Generate all possible combinations of sequences of filled cells with lengths filled_sequences_lengths
    in a string with total length of row_len
    """
    if not filled_sequences_lengths:
        return ['X' * row_len]
    current_sequence = filled_sequences_lengths[0]
    rest_sequences = filled_sequences_lengths[1:]
    remaining_len = sum(rest_sequences) + len(rest_sequences)
    if current_sequence + remaining_len > row_len:
        return []

    result = []
    offset_range = row_len - current_sequence - remaining_len + 1
    for offset in range(offset_range):
        prefix = 'X' * offset + 'O' * current_sequence
        if len(prefix) == row_len:
            result.append(prefix)
        else:
            prefix += 'X'
            for next_subrow in generate_rows(row_len - len(prefix), rest_sequences):
                result.append(prefix + next_subrow)
    return result


def nonogram_row(row_string, clue_numbers):
    """ Solve one row of nonogram. Determine which cell can be filled, unfilled or unknown at the moment """
    possible_rows = generate_rows(len(row_string), clue_numbers)
    matching_rows = []
    for row in possible_rows:
        if is_matches(row, row_string):
            matching_rows.append(row)
    if not matching_rows:
        return None
    result = sum_rows(matching_rows)
    return result


if __name__ == '__main__':
    assert nonogram_row('??????????', [8]) == '??OOOOOO??', 'Simple boxes_1'
    assert nonogram_row('??????????', [4, 3]) == '??OO???O??', 'Simple boxes_2'
    assert nonogram_row('???O????O?', [3, 1]) == 'X??O??XXOX', 'Simple spaces'
    assert nonogram_row('????X?X???', [3, 2]) == '?OO?XXX?O?', 'Forcing'
    assert nonogram_row('O?X?O?????', [1, 3]) == 'OXX?OO?XXX', 'Glue'
    assert nonogram_row('??OO?OO???O?O??', [5, 2, 2]) == 'XXOOOOOXXOOXOOX', 'Joining and splitting'
    assert nonogram_row('????OO????', [4]) == 'XX??OO??XX', 'Mercury'
    assert nonogram_row('???X?', [0]) == 'XXXXX', 'Empty_1'
    assert nonogram_row('?????', []) == 'XXXXX', 'Empty_2'
    assert nonogram_row('??X??', [3]) is None, 'Wrong string'
    print("Check done.")

