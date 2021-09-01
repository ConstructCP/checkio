"""
Transform number to string representation: 42 -> forty two
Input: A number as an integer.
Output: The string representation of the number as a string.
https://py.checkio.org/mission/speechmodule
"""
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def write_hundreds(hundreds: int) -> str:
    """ Return string representation of hundreds part of a number """
    if hundreds == 0:
        return ''
    return (FIRST_TEN[hundreds - 1] + ' ' + HUNDRED).strip()


def write_tens_and_ones(number: int) -> str:
    """ Return string representation of dozens and ones of a number """
    if number == 0:
        return ''
    elif 1 <= number < 10:
        return FIRST_TEN[number - 1]
    elif 10 <= number < 20:
        return SECOND_TEN[number - 10]
    else:
        tens = number // 10
        tens_as_string = OTHER_TENS[tens - 2]
        ones = number % 10
        ones_as_string = FIRST_TEN[ones - 1] if ones > 0 else ''
        return (tens_as_string + ' ' + ones_as_string).strip()


def number_as_string(number: int) -> str:
    """ Return string representation of number < 1000 """
    if number == 0:
        return 'zero'
    hundreds = write_hundreds(number // 100)
    tens_and_ones = write_tens_and_ones(number % 100)
    as_string = (hundreds + ' ' + tens_and_ones).strip()
    return as_string


def checkio(number: int) -> str:
    """ Transform number into string form """
    result = number_as_string(number)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
