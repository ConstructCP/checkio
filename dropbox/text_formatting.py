"""
You are given a long line (a monospace font), and you have to break the line in order to respect a given width.
Then you have to format the text according to the given style: aligh to left/right, center text or justify it.
Lines of the output shouldn’t end with a whitespace.
If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.

The justification rules:
    Since we can't always put the same number of spaces between words in a line, put big blocks of spaces first.
    For example: X---X---X--X--X--X when you have to put 12 spaces in 5 gaps: 3-3-2-2-2.
    Don't justify the last line of a text.

Input: A text (string), width (integer) and style (string).
Output: The formatted text (string).
https://py.checkio.org/en/mission/text-formatting/
"""
from itertools import chain
from typing import List, Iterator


def split_text_by_lines(text: str, line_len: int) -> List[List[str]]:
    splitted_by_lines = []
    current_line = []
    current_line_len = 0
    for word in text.split():
        if current_line_len + len(word) <= line_len:
            current_line.append(word)
            current_line_len = current_line_len + len(word) + 1
        else:
            splitted_by_lines.append(current_line)
            current_line = [word]
            current_line_len = len(word) + 1
    if current_line:
        splitted_by_lines.append(current_line)
    return splitted_by_lines


def justify_string(words: List[str], line_len: int) -> str:
    total_words_len = sum([len(w) for w in words])
    spaces_to_insert = line_len - total_words_len
    spaces_between_words = spaces_to_insert // (len(words) - 1)
    extra_spaces = spaces_to_insert % (len(words) - 1)
    resulting_list = []
    for word in words:
        resulting_list.append(word)
        if extra_spaces:
            spaces = ' ' * (spaces_between_words + 1)
            resulting_list.append(spaces)
            extra_spaces -= 1
        else:
            spaces = ' ' * spaces_between_words
            resulting_list.append(spaces)
    resulting_list.pop()
    result = ''.join(resulting_list)
    return result


def format_text(lines: List[List[str]], width: int, style: str) -> Iterator[str]:
    if style == 'j':
        text_till_last_string = map(lambda s: justify_string(s, width), lines[:-1])
        last_string = ' '.join(lines[-1])
        return chain(text_till_last_string, [last_string])
    else:
        joined = map(lambda l: ' '.join(l), lines)
        if style == 'l':
            formatted = map(lambda s: s.ljust(width, ' '), joined)
        elif style == 'c':
            formatted = map(lambda s: s.center(width, ' '), joined)
        elif style == 'r':
            formatted = map(lambda s: s.rjust(width, ' '), joined)
        return map(lambda s: s.rstrip(), formatted)


def text_formatting(text: str, width: int, style: str) -> str:
    text_by_lines = split_text_by_lines(text, width)
    formatted_by_lines = format_text(text_by_lines, width, style)
    return '\n'.join(formatted_by_lines)


if __name__ == '__main__':
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')

    print('Example:')
    print(text_formatting(LINE, 30, 'c'))

    assert text_formatting(LINE, 38, 'l') == \
        '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa.''', 'Left 38'

    assert text_formatting(LINE, 30, 'c') == \
        ''' Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa.''', 'Center 30'

    assert text_formatting(LINE, 50, 'r') == \
        '''           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa.''', 'Right 50'

    assert text_formatting(LINE, 45, 'j') == \
        '''Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa.''', 'Justify 45'
