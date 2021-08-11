from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    """ Check if items in sequence are in ascending order """
    if len(items) < 2:
        return True
    for prev_item, cur_item in zip(items[:-1], items[1:]):
        if prev_item >= cur_item:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
