from collections import Counter


def frequency_sort(items: list) -> list:
    """
    Sort elements of list by frequency. Most frequent first.
    """
    frequencies = Counter(items)
    sorted_by_freq = sorted(frequencies, key=lambda x: frequencies[x],
                            reverse=True)
    result = []
    for el in sorted_by_freq:
        occurencies = frequencies[el]
        result += [el] * occurencies
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4,4,4,4,6,6,2,2,2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
