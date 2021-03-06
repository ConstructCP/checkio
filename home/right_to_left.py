def left_join(phrases: tuple) -> str:
    """
    Join strings in the tuple using ',' as delimeter and 
    replace all occurencies of "right" to "left".
    """
    result = ''
    for string in phrases:
        replaced_string = string.replace('right', 'left')
        if len(result) != 0:
            result += ','
        result += replaced_string
    return result


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
