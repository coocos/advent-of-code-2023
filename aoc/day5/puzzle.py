from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Range:
    source: int
    destination: int
    length: int


@dataclass
class Transform:
    domain: str
    codomain: str
    ranges: list[Range]


def parse_input() -> tuple[list[int], dict[str, Transform]]:
    lines = (Path(__file__).parent / "input.txt").read_text().split("\n")

    seeds = [int(num) for num in lines[0].split(" ") if num.isdigit()]

    transforms: list[Transform] = []
    for line in lines[1:]:
        if match := re.match(r"(\d+) (\d+) (\d+)", line):
            destination, source, length = [int(n) for n in match.groups()]
            transforms[-1].ranges.append(Range(source, destination, length))
        elif match := re.match(r"(\w+)-to-(\w+) map", line):
            domain, codomain = match.groups()
            transforms.append(Transform(domain, codomain, []))
    return seeds, {transform.domain: transform for transform in transforms}


def part_1(seeds: list[int], transforms: dict[str, Transform]) -> int:
    locations = []
    for value in seeds:
        domain = "seed"
        while domain in transforms:
            transform = transforms[domain]
            for range in transform.ranges:
                if range.source <= value < range.source + range.length:
                    value = range.destination + (value - range.source)
                    break
            domain = transform.codomain
        locations.append(value)
    return min(locations)


def solve() -> None:
    seeds, transforms = parse_input()

    assert part_1(seeds, transforms) == 403695602


if __name__ == "__main__":
    solve()
