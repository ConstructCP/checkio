def first_word(text: str) -> str:
    """
    Returns the first word in a given text.
    """
    word_beginning, word_end = None, None
    for index, symbol in enumerate(text):
        if word_beginning is None and symbol.isalpha():
            word_beginning = index
        if word_beginning is not None:
            if symbol.isalpha() or symbol == "\'":
                continue
            else:
                word_end = index
                break
    return text[word_beginning:word_end]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
