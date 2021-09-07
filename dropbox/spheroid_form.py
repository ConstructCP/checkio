"""
Calculate the volume (cubic inches) and the surface area (square inches) of a spheroid with given height and width.
Input: Two arguments. A height and a width as integers.
Output: The volume and the surface area as a list of floats. The results should be accurate to two decimals.
https://py.checkio.org/mission/humpty-dumpty/
"""
import math
from typing import List


def volume(equatorial_diameter: int, polar_diameter: int) -> float:
    """ Calculate the volume of a spheroid """
    vol = math.pi / 6 * equatorial_diameter ** 2 * polar_diameter
    return vol


def surface_area(equatorial_radius: float, polar_radius: float) -> float:
    """ Calculate the surface area of a spheroid """
    if polar_radius < equatorial_radius:
        e_square = 1 - polar_radius ** 2 / equatorial_radius ** 2
        e = e_square ** 0.5
        sq = 2 * math.pi * equatorial_radius ** 2 * (1 + (1 - e_square) / e * math.atanh(e))
    elif polar_radius == equatorial_radius:
        sq = 4 * math.pi * equatorial_radius ** 2
    else:
        e_square = 1 - equatorial_radius ** 2 / polar_radius ** 2
        e = e_square ** 0.5
        sq = 2 * math.pi * equatorial_radius ** 2 * (1 + polar_radius / (equatorial_radius * e) * math.asin(e))
    return sq


def checkio(height: int, width: int) -> List[float]:
    """ Calculate volume and square of surface area of a spheroid with given width and height """
    vol = volume(width, height)
    sq = surface_area(width / 2, height / 2)
    return [round(vol, 2), round(sq, 2)]


if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"