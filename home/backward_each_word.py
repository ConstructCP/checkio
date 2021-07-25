import re


def backward_string_by_word(text: str) -> str:
    """
    Reverse each word in the string
    """
    backwarded = []
    for sequence in re.findall(r'\w+|\W+', text):
        if sequence.isalpha():
            backwarded.append(sequence[::-1])
        else:
            backwarded.append(sequence)

    return ''.join(backwarded)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('hi all!'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game!') == 'emoclew ot a emag!'
    print("Coding complete? Click 'Check' to earn cool rewards!")
