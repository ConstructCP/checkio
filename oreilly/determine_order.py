from typing import List


def checkio(data: List[str]) -> str:
    """
    Determine order of symbols by data strings. Data consists of several strings
    where symbols are ordered in non-alphabetical order.
    """
    before, after = {}, {}
    to_order = set()
    for string in data:
        string = remove_duplicates(string)
        for i, char in enumerate(string):
            if i > 0:
                before[char] = before.get(char, list())
                if string[i - 1] not in before[char]:
                    before[char].append(string[i - 1])
            if i < len(string) - 1:
                after[char] = after.get(char, list())
                if string[i + 1] not in after[char]:
                    after[char].append(string[i + 1])
            to_order.add(char)
    order = []
    chars_without_predeccessors = sorted([char for char in to_order if before.get(char, None) is None])
    for head in chars_without_predeccessors:
        for after_head in after.get(head, list()):
            if after_head in order:
                insert_index = order.index(after_head)
                order.insert(insert_index, head)
                break
        if head in order:
            break
        else:
            order.append(head)
        while next_item := get_next(order[-1], after):
            order.append(next_item)
    return ''.join(order)


def remove_duplicates(s: str) -> str:
    """ Remove duplicating symbols from string with order preserved"""
    uniques_as_list = sorted(set(s), key=lambda c: s.index(c))
    return ''.join(uniques_as_list)


def get_next(item: str, after: dict) -> str:
    """
    Determine next symbol from list of folowers. Check if some of followers has another
    as a follower of self. otherwise sort in alphabetical order
    """
    item_followers = after.get(item, None)
    if item_followers is None:
        return None
    if len(item_followers) == 1:
        return item_followers[0]
    else:
        for item in item_followers:
            if all(is_predeccessor(after, item, x) for x in item_followers if item is not x):
                return item
        else:
            item_followers.sort()
            to_return = item_followers[0]
            after[to_return].extend(item_followers[1:])
            return to_return


def is_predeccessor(after: dict, predeccessor: str, follower: str) -> bool:
    """ Determine if on symbol has another as a follower in chain of followers """
    all_followers = after.get(predeccessor, None)
    if all_followers is None:
        return False
    all_followers = list(all_followers)
    while all_followers:
        if follower in all_followers:
            return True
        item = all_followers.pop(0)
        if new_followers := after.get(item, None):
            all_followers.extend(new_followers)
    return False


if __name__ == '__main__':
    print(
        checkio(["jhgfdba", "jihcba", "jigedca"])
    )

    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
