from collections import Counter


def is_majority(items: list) -> bool:
    """
    Check if majority of elements is True. Return False in case of equal
    number of True and False. Return False for empty list
    """
    count = Counter(items)
    return count.get(True, 0) > count.get(False, 0)


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
