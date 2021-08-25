from itertools import combinations


def checkio(words_set: set) -> bool:
    """ Find whether there are 2 words in a set, one of which is the end of another """
    for word1, word2 in combinations(words_set, r=2):
        if word1.endswith(word2) or word2.endswith(word1):
            return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
