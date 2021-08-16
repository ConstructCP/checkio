from collections import Counter


def isometric_strings(a: str, b: str) -> bool:
    """
    Check if strings are isometric:  all characters of string a must have
    a match in string b. Several characters from a can have 1 match in b, but
    not vice versa.
    """
    replacements = {}
    for a_char, b_char in zip(a, b):
        repl = replacements.get(a_char, None)
        if repl is None:
            replacements[a_char] = b_char
        elif repl == b_char:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
