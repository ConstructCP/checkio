def between_markers(text: str, begin: str, end: str) -> str:
    """
    Return part of string between given markers.
    If begin marker is not found - return substring from the beginning to end marker.
    If end marker not found - return substring from begin marker to end.
    If both marker weren't found - return the whole string
    """
    pos_begin = text.find(begin)
    pos_end = text.find(end)
    if pos_begin < 0:
        pos_begin = None
    else:
        pos_begin += len(begin)
    if pos_end < 0:
        pos_end = None
    return text[pos_begin:pos_end]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
