def second_index(text: str, symbol: str) -> [int, None]:
    """
    Return the second index of a symbol in a given text. 
    Return None in case of 0 or 1 occurencies of symbol in a text.
    """
    first_index = text.find(symbol)
    print(text[first_index + 1:])
    substring_index = text[first_index + 1:].find(symbol)
    if substring_index != -1:
        second_index = substring_index + first_index + 1
        return second_index
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
