from collections import Counter


def non_unique_elements(data: list) -> list:
    """
    Return list with all non-unique elements from input data
    """
    count = Counter(data)

    non_unique_data = []
    for i in data:
        if count[i] > 1:
            non_unique_data.append(i)
    return non_unique_data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
