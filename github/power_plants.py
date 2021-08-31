"""
The intercity network and the range of each power plant are given as input values. A power plant
can provide power to the city where it’s been placed and within its range.
You have to return a dictionary, where the key is the city in which you’ll place the power plant
and the value is its range. You will always be given enough or more power-plants.

Input: the intercity network represented as a set of connections, where each connection is
a tuple of two nodes connected with each other. The range of each power plant, represented
as a list of integers.
Output: a dictionary of placements, where each key is the city in which you’ll place
the power plant and each value is the corresponding range.
https://py.checkio.org/mission/power-plants/solve/
"""
from typing import Set, Tuple, List, Dict, Union


class City:
    def __init__(self, name: str) -> None:
        """ Initialize city with given name and empty connections list"""
        self.name = name
        self.connections = []

    def add_connection(self, connected_city: 'City') -> None:
        """ Add connection to connection list """
        self.connections.append(connected_city)

    def get_cities_in_range(self, reach_range: int) -> Set['City']:
        """ Get set of cities that lie within given range from this city """
        if reach_range == 0:
            return {self}
        elif reach_range == 1:
            return set(self.connections)
        else:
            reachable = set()
            for conn in self.connections:
                reachable |= {conn}
                reachable_from_conn = conn.get_cities_in_range(reach_range - 1)
                reachable |= reachable_from_conn
            reachable.remove(self)
            return reachable

    def __repr__(self) -> str:
        """ Object representation for debug """
        return self.name


def create_network(connections: Set[Tuple[str, str]]) -> Dict[str, City]:
    """ Create cities objects, add connections between them """
    network = {}
    for city1, city2 in connections:
        if city1 not in network:
            network[city1] = City(city1)
        if city2 not in network:
            network[city2] = City(city2)
        network[city1].add_connection(network[city2])
        network[city2].add_connection(network[city1])
    return network


def get_cities_coverage(network: Dict[str, City], rng: int) -> Dict[str, Set[str]]:
    """ For all the cities build a dict of reachable cities within given range """
    coverages = {}
    for name, city in network.items():
        city_coverage = city.get_cities_in_range(rng)
        coverages[name] = {city.name for city in city_coverage}
    return coverages


def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    """ Define the location of power plants that so that all cities in network can be powered """
    plants = {}
    city_network = create_network(network)
    all_cities = set(city_network.keys())
    ranges_coverages = {}
    for r in set(ranges):
        ranges_coverages[r] = get_cities_coverage(city_network, r)

    plant_places = recursive_cover_all_cities(city_network, all_cities, set(), ranges_coverages, ranges, [])
    result = {city: rng for city, rng in zip(plant_places, ranges)}
    return result


def recursive_cover_all_cities(city_network: Dict[str, City], target_cov: Set[str], cur_cov: Set[str],
                               range_cov: Dict[str, Set[str]], ranges: List[int],
                               call_stack: List[str]) -> Union[List[str], None]:
    """ Recursively try to find combinations of cities that will give target coverage """
    cur_range = ranges[0]
    for city_name, city_cov in range_cov[cur_range].items():
        call_stack.append(city_name)
        cov_with_city = city_cov | {city_name} | cur_cov
        if cov_with_city == target_cov:
            return call_stack
        else:
            left_ranges = ranges[1:]
            if left_ranges:
                next_level_call_result = recursive_cover_all_cities(city_network, target_cov, cov_with_city, range_cov, left_ranges, call_stack)
                if next_level_call_result:
                    return next_level_call_result
        call_stack.pop()
    return None


if __name__ == '__main__':
    print(
        power_plants([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["A", "F"], ["F", "G"], ["G", "H"]], [2, 1])
    )
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')
