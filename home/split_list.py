def split_list(items: list) -> list:
    # find the middle number
    #     - check len is even
    #     - calc position of middle element
    # create 2 lists

    is_len_even = len(items) % 2 == 0
    if is_len_even:
        middle_element_pos = len(items) // 2
    else:
        middle_element_pos = len(items) // 2 + 1

    left_list, right_list = items[:middle_element_pos], items[middle_element_pos:]
    return left_list, right_list


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
