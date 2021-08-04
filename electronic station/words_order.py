from itertools import dropwhile

def words_order(text: str, words: list) -> bool:
    """
    Check if words in list appear in text in the same order.
    If any 2 words in list are the same - return false
    """
    if any([words[0] == word for word in words[1:]]):
        return False
    it = iter(text.split())
    for next_word in words:
        try:
            it = dropwhile(lambda word: word != next_word, it)
            next(it)
        except StopIteration:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'im', 'here']) == True
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
