from typing import List


def find_destinations(routes: List, departure_point: str) -> List:
    """ Find all possible destinations from departure point """
    destinations = []
    for route in routes:
        if departure_point in route:
            dest = route[0] if route[0] is not departure_point else route[1]
            destinations.append(dest)
    return destinations


def find_travel_cost(costs: List, frm: str, to: str) -> int:
    for route in costs:
        if frm in route and to in route:
            return route[2]


def cheapest_flight(costs: List, a: str, b: str) -> int:
    """ Find cheapest route between points a and b """
    total = []

    def depth_search(current_point: str, target: str, visited: List, travel_cost: int = 0) -> None:
        """
        Recursively search for route to target.
        If route is found, append it to total from enclosing scope
        """
        for dest in find_destinations(costs, current_point):
            if dest == target:
                total.append(travel_cost + find_travel_cost(costs, current_point, dest))
            else:
                if dest not in visited:
                    depth_search(dest, target,
                                 visited + [current_point],
                                 travel_cost + find_travel_cost(costs, current_point, dest))

    depth_search(a, b, [], 0)
    if len(total):
        return min(total)
    else:
        return 0


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
                           ['A', 'B', 20],
                           ['B', 'C', 50]],
                          'A',
                          'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'A',
                           'C') == 70
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'C',
                           'A') == 70
    assert cheapest_flight([['A', 'C', 40],
                            ['A', 'B', 20],
                            ['A', 'D', 20],
                            ['B', 'C', 50],
                            ['D', 'C', 70]],
                           'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['D', 'F', 900]],
                           'A',
                           'F') == 0
    assert cheapest_flight([['A', 'B', 10],
                            ['A', 'C', 15],
                            ['B', 'D', 15],
                            ['C', 'D', 10]],
                           'A',
                           'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
