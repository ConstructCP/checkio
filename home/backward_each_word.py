def backward_string_by_word(text: str) -> str:
    i = 0
    backwarded_text = ''
    while i < len(text):
        is_letter = text[i].isalpha()
        if is_letter:
            word_beg = i - 1
            while i < len(text) and text[i].isalpha():
                i += 1
            word_end = i - 1
            if word_beg <= 0:
                backwarded_text += text[word_end::-1]
            else:
                backwarded_text += text[word_end:word_beg:-1]
        else:
            backwarded_text += text[i]
            i += 1
    return backwarded_text

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game!') == 'emoclew ot a emag!'
    print("Coding complete? Click 'Check' to earn cool rewards!")
