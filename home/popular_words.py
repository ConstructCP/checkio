def popular_words(text: str, words: list) -> dict:
    """
    Calculate how many times given words appear in text. Return dict in form {"word": occurencies}
    """
    counter = {search_word: 0 for search_word in words}
    for word in text.split():
        word = word.lower()
        if word in counter:
            counter[word] += 1
    return counter


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
