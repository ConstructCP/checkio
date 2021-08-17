from itertools import dropwhile
from collections import deque
from typing import Iterator, Any


class RegexProcessingError(Exception):
    pass


def get_next(iterator: Iterator) -> Any:
    """ Get next item from iterator. Return None if operator is exhausted """
    try:
        return next(iterator)
    except StopIteration:
        return None


def exhaust_iterator(iterator: Iterator) -> None:
    """ Exhaust iterator """
    deque(iterator, maxlen=0)


def process_asterisk(regex_iter: Iterator, match_iter: Iterator) -> None:
    """ Handle asterisk symbol in regex. """
    # Skip regex until next non-special symbol or end is found or until iterator is exhausted.
    #while next_pattern_char := get_next(regex_iter):
    while True:
        next_pattern_char = get_next(regex_iter)
        if next_pattern_char is None:
            # if * is the last regex symbol - exhaust match_iter
            exhaust_iterator(match_iter)
            return
        if next_pattern_char not in '*?':
            # Skip all symbols from match iterator until symbol from regex is found
            file_it = dropwhile(lambda char: char != next_pattern_char, match_iter)
            # Raise exception if next symbol from regex wasn't found
            if get_next(file_it) is None:
                raise RegexProcessingError


def process_question_mark(match_it: Iterator) -> None:
    """ Process ? in regex. Get any symbol or raise exception if iterator is exhausted """
    next_match_symbol = get_next(match_it)
    if next_match_symbol is None:
        raise RegexProcessingError


def unix_match(filename: str, pattern: str) -> bool:
    """
    Check if filename matches pattern.
    ? in pattern means any symbol
    * in pattern means sequence of any symbols
    """
    pattern_it = iter(pattern)
    file_it = iter(filename)
    while True:
        pattern_char = get_next(pattern_it)
        try:
            if pattern_char == '*':
                process_asterisk(pattern_it, file_it)
            elif pattern_char == '?':
                process_question_mark(file_it)
            elif pattern_char is None:
                # End of pattern. Check if filename is also at end
                if get_next(file_it) is None:
                    break
                else:
                    raise RegexProcessingError
            else:
                file_char = get_next(file_it)
                if not pattern_char == file_char:
                    raise RegexProcessingError
        except RegexProcessingError:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
