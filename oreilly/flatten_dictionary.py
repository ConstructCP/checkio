from typing import Union, List


def flatten(dictionary: dict) -> dict:
    """ Remove nested dictionaries and replace them as outer_dict/nested_dict : key """

    flattened_dict = get_keys(dictionary)
    return flattened_dict


def get_keys(to_flatten: dict, key_stack: Union[List, None] = None) -> dict:
    if key_stack is None:
        key_stack = []
    flattened = {}
    if len(to_flatten.values()) == 0:
        flattened_key = '/'.join(key_stack)
        flattened[flattened_key] = ""
        return flattened
    for key, item in to_flatten.items():
        key_stack.append(key)
        if isinstance(item, dict):
            flattened_nested = get_keys(item, key_stack)
            flattened.update(flattened_nested)
        else:
            flattened_key = '/'.join(key_stack)
            flattened[flattened_key] = item
        key_stack.pop()
    return flattened


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
