from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """
    Check if all files in list are the same
    """
    if len(elements) == 0:
        return True

    first = elements[0]
    return all(x == first for x in elements[1:])


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
