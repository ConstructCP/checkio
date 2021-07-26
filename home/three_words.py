def has_3_words_in_succession(words: str) -> bool:
    """
    Determine if given text has 3 words in succession
    """
    words_sequence_len = 0
    for word in words.split():
        if word.isalpha():
            words_sequence_len += 1
        else:
            words_sequence_len = 0
        if words_sequence_len == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert has_3_words_in_succession("Hello World hello") == True, "Hello"
    assert has_3_words_in_succession("He is 123 man") == False, "123 man"
    assert has_3_words_in_succession("1 2 3 4") == False, "Digits"
    assert has_3_words_in_succession("bla bla bla bla") == True, "Bla Bla"
    assert has_3_words_in_succession("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
