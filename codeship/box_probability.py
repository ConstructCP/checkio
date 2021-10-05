"""
There are white and black pearls in the box. Each turn pearl of random color
is taken from the box and replaces the opposite color. Calculate probability of
getting a white pearl on N-th turn
Input: The start sequence of the pearls as a string and the move number as an integer.
Output: The probability for a white pearl as a float.
https://py.checkio.org/mission/box-probability
"""
from collections import Counter
from typing import List


def play_game(starting_pearls: str, turn_limit: int) -> float:
    """ Calculate probability of getting white pearl after turn limit is reached """
    probabilities_of_white = []

    def game_turn(pearls_in_the_box: str, turn_number: int, variant_probability: float) -> None:
        """
        Calculate probability of black and white pearl on turn. If turn limit is reached -
        add probability of white to sum of probabilities. If not - proceed with next turn
        """
        white_num = pearls_in_the_box.count('w')
        total_num = len(pearls_in_the_box)
        white_prob = white_num / total_num
        black_prob = (total_num - white_num) / total_num
        if turn_number == turn_limit:
            probabilities_of_white.append(white_prob * variant_probability)
        else:
            if white_prob > 0:
                new_config = pearls_in_the_box.replace('w', 'b', 1)
                game_turn(new_config, turn_number + 1, white_prob * variant_probability)
            if black_prob > 0:
                new_config = pearls_in_the_box.replace('b', 'w', 1)
                game_turn(new_config, turn_number + 1, black_prob * variant_probability)

    game_turn(starting_pearls, 1, 1)
    return sum(probabilities_of_white)


def checkio(marbles: str, step: int) -> float:
    """
    Play game, calculate probability of getting white pearl on given step.
    Return result rounded to two decimal digits of precision
    """
    probability_of_white = play_game(marbles, step)
    return round(probability_of_white, 2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
