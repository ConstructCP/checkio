from typing import Iterator, Tuple, Any, Set


class RegexProcessingError(Exception):
    pass


def get_next(iterator: Iterator) -> Any:
    """ Get next item from iterator. Return None if operator is exhausted """
    try:
        return next(iterator)
    except StopIteration:
        return None


def get_symbols_in_square_brackets(pattern_iter: Iterator) -> Tuple[Set, bool]:
    """
    Get set of symbols from pattern's square brackets. If ! is first symbol - mark sequence as excluding
    """
    is_excluding = False
    char_set = set()
    char = get_next(pattern_iter)
    if char == '!':
        is_excluding = True
    else:
        char_set.add(char)

    while True:
        char = get_next(pattern_iter)
        if char == ']':
            break
        elif char is None:
            # Closing bracket wasn't found
            raise RegexProcessingError('Closing bracket not found')
        else:
            char_set.add(char)

    return char_set, is_excluding


def handle_square_brackets_edge_cases(has_exclamation_mark, match_iter):
    edge_case_seq = '[!]' if has_exclamation_mark else '[]'
    for c in edge_case_seq:
        file_char = get_next(match_iter)
        if file_char != c:
            raise RegexProcessingError


def unix_match(filename: str, pattern: str) -> bool:
    """
    Check if filename matches pattern.
    [seq] matches any character in seq, for example [123] means any character - '1', '2' or '3'
    [!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
    [] seq without any chars will never match
    """
    pattern_it = iter(pattern)
    file_it = iter(filename)
    while True:
        try:
            pattern_char = get_next(pattern_it)
            if pattern_char == '[':
                char_set, is_excluding = get_symbols_in_square_brackets(pattern_it)
                if len(char_set) == 0:
                    # [] and [!] are not considered symbol sets
                    handle_square_brackets_edge_cases(is_excluding, file_it)
                    continue
                file_char = get_next(file_it)
                if (is_excluding and file_char in char_set) or (not is_excluding and file_char not in char_set):
                    raise RegexProcessingError
            elif pattern_char is None:
                if get_next(file_it) is None:
                    return True
                else:
                    raise RegexProcessingError
            else:
                file_char = get_next(file_it)
                if not pattern_char == file_char:
                    raise RegexProcessingError
        except RegexProcessingError:
            return False


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
