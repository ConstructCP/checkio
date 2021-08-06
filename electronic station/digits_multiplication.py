def multiply_digits(number: int) -> int:
    """Calculate product of all digits in given number. Ignore zeros"""
    if number == 0:
        return 0
    product = 1
    for digit in str(number):
        if digit == '0':
            continue
        product *= int(digit)
    return product


if __name__ == '__main__':
    print('Example:')
    print(multiply_digits(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert multiply_digits(123405) == 120
    assert multiply_digits(999) == 729
    assert multiply_digits(1000) == 1
    assert multiply_digits(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
