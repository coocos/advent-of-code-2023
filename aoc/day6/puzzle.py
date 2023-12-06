import math
from pathlib import Path
from functools import reduce
import re

Race = tuple[int, int]


def parse_input() -> list[Race]:
    lines = (Path(__file__).parent / "input.txt").read_text().splitlines()
    durations = [int(num) for num in re.findall(r"(\d+)", lines[0])]
    records = [int(num) for num in re.findall(r"(\d+)", lines[1])]
    return list(zip(durations, records))


def part_1(races: list[Race]) -> int:
    won = []
    for duration, record in races:
        won.append(
            sum(1 for time in range(1, duration) if time * (duration - time) > record)
        )
    return math.prod(won)


def part_2(races: list[Race]) -> int:
    duration, record = reduce(
        lambda combo, race: (combo[0] + str(race[0]), combo[1] + str(race[1])),
        races,
        ("", ""),
    )
    return part_1([(int(duration), int(record))])


def solve() -> None:
    races = parse_input()

    assert part_1(races) == 4403592

    assert part_2(races) == 38017587


if __name__ == "__main__":
    solve()
