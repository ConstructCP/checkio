from typing import Union


def mins_from_sunrise(hours: int, mins: int) -> int:
    """Calculate minutes passed after sunrise"""
    return (hours - 6) * 60 + mins


def is_daytime(hours: int, mins: int) -> bool:
    """Checks if given time is daytime"""
    if hours < 6: return False
    if hours >= 18 and mins > 0: return False
    return True


def sun_angle(time: str) -> Union[int, str]:
    """
    Calculate angle of the sun basing on time.
    6:00 - 0', 12:00 - 90'? 18:00 - 180'
    If time is between 18:00 and 6:00 - return "I don't see the sun!".
    """
    hours, mins = map(int, time.split(':'))
    if not is_daytime(hours, mins):
        return "I don't see the sun!"

    current = mins_from_sunrise(hours, mins)
    sunset = mins_from_sunrise(18, 00)
    return current * 180 / sunset


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("12:15"))

    # These "asserts" using only for self-checking and not necessary for auto-testing

    sun_angle("07:00") == 15
    sun_angle("12:15") == 93.75
    sun_angle("01:23") == "I don't see the sun!"
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
