def flat_list(array: list) -> list:
    """ Extract items from nested lists and preserve items order """
    result = []
    for item in array:
        if isinstance(item, list):
            flat_nested = flat_list(item)
            result.extend(flat_nested)
        else:
            result.append(item)
    return result


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')