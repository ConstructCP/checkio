from datetime import datetime
from typing import List, Optional


def timedelta_seconds(start: datetime, stop: datetime) -> int:
    delta = (stop - start).total_seconds()
    if delta > 0:
        return int(delta)
    else:
        return 0


def sum_light(switches: List[datetime], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    """
    Calculate total number of seconds the light bulb was turned on
    between watch_start and watch_end.
    """
    if start_watching is None:
        start_watching = datetime.min
    if end_watching is None:
        end_watching = datetime.max
    turned_on = None
    time_turned_on = 0
    for switch in switches:
        if turned_on is None:
            turned_on = switch
        else:
            time_turned_on += timedelta_seconds(start=max(start_watching, turned_on), stop=min(end_watching, switch))
            turned_on = None
    if turned_on is not None:
        time_turned_on += timedelta_seconds(start=max(start_watching, turned_on), stop=end_watching)
    return time_turned_on


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light([
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 10, 10),
            datetime(2015, 1, 12, 11, 0, 0)
        ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 11, 10, 0)
        )
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )
    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")