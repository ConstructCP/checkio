"""
Calculate hash of the string
Input: Two arguments. A string to be hashed and a hash algorithm as a string (unicode utf8).
Algorithm in ("md5", "sha224", "sha256", "sha384", "sha512", "sha1")
Output: Hexadecimal hash for for input string using given algorithm as a string.
https://py.checkio.org/mission/simple-hashlib/
"""


import hashlib


def checkio(string_to_hash: str, algorithm: str) -> str:
    """ Calculate hash of the string """
    hash_functions = {"md5": hashlib.md5, "sha224": hashlib.sha224,
                      "sha256": hashlib.sha256, "sha384": hashlib.sha384,
                      "sha512": hashlib.sha512, "sha1": hashlib.sha1}
    hashed_string = hash_functions[algorithm](string_to_hash.encode('utf-8')).hexdigest()
    return hashed_string


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
