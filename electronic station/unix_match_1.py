from itertools import dropwhile
from collections import deque
from typing import Iterator, Any


def unix_match(filename: str, pattern: str) -> bool:
    """
    Check if filename matches pattern.
    ? in pattern means any symbol
    * in pattern means sequence of any symbols
    """
    filename_index = 0
    is_asterisk = False
    for pattern_symbol in pattern:
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
        else:
            if pattern_symbol != filename[filename_index]:
                return False
            filename_index += 1
    return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match('file', 'file?'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
