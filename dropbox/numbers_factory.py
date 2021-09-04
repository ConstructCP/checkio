"""
Find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist,
then return 0. Example: N = 20. We can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225,
for 4*5 - 45. So we select 45.
Input: A number N as an integer.
Output: The number X as an integer.
https://py.checkio.org/mission/number-factory
"""
from typing import List, Generator


def primes() -> Generator[int]:
    """ Generates prime numbers """
    prime_nums = [1, 2]
    n = 2
    while True:
        n += 1
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_nums.append(n)
            yield n
            

def is_prime(x: int) -> bool:
    """ Check if given number is prime number """
    prime_gen = primes()
    for val in prime_gen:
        if val == x:
            return True
        elif val > x:
            return False


def find_product(number: int) -> List[List[int]]:
    """ Find all combination of digits product of which can be the given number """
    products = []
    for i in range(2, 10):
        if number % i == 0:
            remainder = number // i
            if remainder == 1:
                products.append([i])
            else:
                remainder_products = find_product(remainder)
                if remainder_products:
                    for p in remainder_products:
                        p.append(i)
                        products.append(p)
    removed_duplicates = []
    for item in products:
        if sorted(item) not in removed_duplicates:
            removed_duplicates.append(sorted(item))
    return removed_duplicates


def construct_lowest_number(digits_lists: List[List[int]]) -> int:
    """ From lists of digits construct the lowest possible numbers and return minimum """
    numbers = []
    for digit_list in digits_lists:
        digit_list.sort()
        num = int(''.join(str(digit) for digit in digit_list))
        numbers.append(num)
    return min(numbers)


def checkio(number: int) -> int:
    """ Find the smallest positive number, such that the product of its digits is equal to given number """
    if is_prime(number):
        return 0
    all_products = find_product(number)
    if all_products:
        num = construct_lowest_number(all_products)
        return num
    else:
        return 0



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")