from datetime import datetime

def days_diff(date1: (int, int, int), date2: (int, int, int)) -> int:
    """
    Calculate difference between given 2 dates in days
    """
    date1 = datetime(*date1)
    date2 = datetime(*date2)
    diff = date1 - date2
    return abs(diff.days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
