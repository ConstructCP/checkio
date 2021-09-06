"""
Yo have three rotating levers.
If you rotate the first, then the second is rotated f2 times faster, the third - at the f3 time faster.
If you rotate the second, then the third is rotated s3 times faster, the first - at the s1 time faster.
If you rotate the third, then the first is rotated t1 times faster, the second - at the t2 time faster.
This correlation can be represented as a matrix 3x3 with 1 in the main diagonal.
[[1 	f2  f3]
 [s1 	1   s3]
 [t1 	t2 	1]]
You can rotate each lever once in the following order: the first, the second, the third.
Levers start in angles [0, 0, 0]. You need to put levers in the following angles: [0, 225, 315]
https://py.checkio.org/en/mission/hubspot-amulet/
"""
from itertools import product
from typing import List, Tuple, Iterable, Iterator

TARGET_ANGLE1 = 0
TARGET_ANGLE2 = 225
TARGET_ANGLE3 = 315


def rotate(starting_angle: int, rotation_angle: int, multiplier: int = 1) -> int:
    """ Rotate the lever on given angle with given multiplier """
    new_angle = starting_angle + rotation_angle * multiplier
    new_angle %= 360
    return new_angle


def rotate_several_times(starting_angle: int, rotation_angles: Iterable[int], multipliers: Iterable[int]) -> int:
    """ Perform several lever rotations with multipliers """
    angle = starting_angle
    for rot, mul in zip(rotation_angles, multipliers):
        angle = rotate(angle, rot, mul)
    return angle


def angles() -> Iterator[Tuple[int, int, int]]:
    """ Generates angles from -180 to 180 """
    return ((a1, a2, a3) for a1, a2, a3 in product(range(-180, 181), range(-180, 181), range(-180, 181)))


def find_rotate_angles(starting_angle: int, target_angle: int,
                       multipliers: Iterable[int]) -> Iterator[Tuple[int, int, int]]:
    """ Try to find rotation angles (with multipliers) for the lever that give target angle """
    for rotate_angles in angles():
        angle = rotate_several_times(starting_angle, rotate_angles, multipliers)
        if angle == target_angle:
            yield rotate_angles


def checkio(matrix: List[List[int]]) -> Tuple[int, int, int]:
    """ Find rotation angles for each lever so that in the end lever angles will be equal to target angles """
    for rotate_angles in find_rotate_angles(0, TARGET_ANGLE1, [matrix[x][0] for x in range(3)]):
        if rotate_several_times(0, rotate_angles, [matrix[x][1] for x in range(3)]) == TARGET_ANGLE2:
            if rotate_several_times(0, rotate_angles, [matrix[x][2] for x in range(3)]) == TARGET_ANGLE3:
                return rotate_angles


if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
