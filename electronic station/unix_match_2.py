from typing import Iterator, Tuple, Any, Set, Union


square_brackets_exclusion_str = '[!]'


def square_brackets_exclusion(filename: str, pattern: str, filename_index: int, pattern_index: int) -> Union[int, None]:
    sequence_len = len(square_brackets_exclusion_str)
    if pattern[pattern_index:pattern_index + sequence_len] == square_brackets_exclusion_str:
        if filename[filename_index:filename_index + sequence_len] == square_brackets_exclusion_str:
            return sequence_len
        else:
            return None


def square_brackets_get_sequence(pattern: str, pattern_index: int) -> Tuple[bool, set]:
    sequence = set()
    is_excluding = False
    pattern_index += 1
    while pattern[pattern_index] != ']':
        if pattern[pattern_index] == '!':
            is_excluding = True
        else:
            sequence.add(pattern[pattern_index])
        pattern_index += 1
    return is_excluding, sequence


def unix_match(filename: str, pattern: str) -> bool:
    """
    Check if filename matches pattern.
    ? in pattern means any symbol
    * in pattern means sequence of any symbols
    [seq] matches any character in seq, for example [123] means any character - '1', '2' or '3'
    [!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
    [] seq without any chars will never match
    """
    """
       Check if filename matches pattern.
       ? in pattern means any symbol
       * in pattern means sequence of any symbols
       """
    filename_index, pattern_index = 0, 0
    is_asterisk = False

    while pattern_index < len(pattern):
        pattern_symbol = pattern[pattern_index]

        if is_asterisk and pattern_symbol != '*':
            while filename[filename_index] != pattern_symbol:
                filename_index += 1
                if filename_index >= len(filename):
                    return False
            is_asterisk = False

        if pattern_symbol == '?':
            if is_asterisk:
                continue
            if filename_index >= len(filename):
                return False
            filename_index += 1
        elif pattern_symbol == '*':
            is_asterisk = True
        elif pattern_symbol == '[':
            if skip_len := square_brackets_exclusion(filename, pattern, filename_index, pattern_index):
                filename_index += skip_len
                pattern_index += skip_len
                continue

            is_excluding, sequence = square_brackets_get_sequence(pattern, pattern_index)
            if ((filename[filename_index] in sequence and not is_excluding) or
                    (filename[filename_index] not in sequence and is_excluding)):
                filename_index += 1
                pattern_index = pattern_index + len(sequence) + 2 + is_excluding
                continue
            else:
                return False
        else:
            if pattern_symbol != filename[filename_index]:
                return False
            filename_index += 1
        pattern_index += 1
    return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match('[!]check.txt', '[!]check.txt'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
