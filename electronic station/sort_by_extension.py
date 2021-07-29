from typing import List


def parse_filename(full_name: str) -> (str, str):
    """
    Parses full file name into actual name and extension parts.
    Names like '.qwe' are considered files without extension

    """
    extension_point = full_name.rfind('.')
    if extension_point == 0:
        extension_point = len(full_name)
    file_name = full_name[:extension_point]
    extension = full_name[extension_point + 1:]
    return file_name, extension


def sort_by_ext(files: List[str]) -> List[str]:
    """Sort files by extension. No extension go first"""
    parsed_names = {name: parse_filename(name) for name in files}
    sorted_names = dict(sorted(parsed_names.items(), key=lambda item: (item[1][1], item[1][0])))
    return list(sorted_names.keys())


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
