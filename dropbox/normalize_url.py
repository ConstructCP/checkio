"""
Normalize URL. Rules:
    1. Converting the scheme and host to lower case:
    HTTP://www.Example.com/ → http://www.example.com/
    2. Capitalizing letters in escape sequences. All letters within a percent-encoding triplet (e.g., "%3B") are
    case-insensitive, and should be capitalized.
    http://www.example.com/a%c2%b1b → http://www.example.com/a%C2%B1b
    3. Decoding percent-encoded octets of unreserved characters. For consistency, percent-encoded octets in the ranges
    of ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde (%7E)
    should not be created by Uniform Resource Identifiers (URI) producers and, when found in a URI,
    should be decoded to their corresponding unreserved characters by URI normalizers.
    http://www.example.com/%7Eusername/ → http://www.example.com/~username/
    4. Removing the default port. The default port (port 80 for the “http” scheme) should be removed from a URL.
    http://www.example.com:80/bar.html → http://www.example.com/bar.html
    5. Removing dot-segments. The segments “..” and “.” can be removed from a URL according to the algorithm described
    in RFC 3986 (or a similar algorithm). ".." is a parent directory, "." is the same directory.
    http://www.example.com/a/b/../c/./d.html → http://www.example.com/a/c/d.html
Input: URL, an unicode string.
Output: Normalized URL, a string.
https://py.checkio.org/mission/url-normalization
"""
import re
from typing import List


def remove_dot_sequences(url: str) -> str:
    """ Remove "." and ".." from url. ".." is a parent directory, "." is the same directory. """
    stack = []
    for part in url.split('/'):
        if part == '.':
            continue
        elif part == '..':
            stack.pop()
        else:
            stack.append(part)
    return '/'.join(stack)


def remove_default_port(url: str) -> str:
    """ Remove default port :80 if it is in url """
    default_port = ':80'
    if default_port in url:
        extract_begin = url.find(default_port)
        extract_end = extract_begin + len(default_port)
        if extract_end == len(url):
            return url[:extract_begin]
        elif url[extract_end] == '/':
            return url[:extract_begin] + url[extract_end:]
    return url


def get_unreserved_symbols() -> List[int]:
    """
    Get list of unreserved symbols given in task
    ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde (%7E)
    """
    alpha_range_high = range(0x41, 0x5A + 1)
    alpha_range_low = range(0x61, 0x7A + 1)
    digit_range = range(0x30, 0x39 + 1)
    other_unreserved = [0x2D, 0x2E, 0x5F, 0x7E]
    unreserved_symbols = list(alpha_range_high) + list(alpha_range_low) + list(digit_range) + other_unreserved
    return unreserved_symbols


def remove_unreserved_escapes(url: str) -> str:
    """ Remove symbol escapes that are not reserved as special characters. """
    escapes_in_url = find_url_escapes(url)
    if escapes_in_url:
        unreserved_symbols = get_unreserved_symbols()
        for escape in escapes_in_url:
            symbol_code = int(escape[1:], base=16)
            if symbol_code in unreserved_symbols:
                url = url.replace(escape, chr(symbol_code))
    return url


def capitalize_escapes(url: str) -> str:
    """ Capitalize all escape sequences in url """
    for escape in find_url_escapes(url):
        url = url.replace(escape, escape.upper())
    return url


def find_url_escapes(url: str) -> List[str]:
    """ Find all escape sequences in URL """
    return re.findall('%[0-9A-Fa-f]{2}', url)


def checkio(url: str) -> str:
    """ Normalize given url """
    url = remove_dot_sequences(url)
    url = remove_default_port(url)
    url = remove_unreserved_escapes(url)
    url = url.lower()
    url = capitalize_escapes(url)
    return url


if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
