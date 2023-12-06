from dataclasses import dataclass, field
import math
from pathlib import Path
import re
from typing import Iterable


@dataclass(frozen=True)
class Vector:
    x: int
    y: int


@dataclass(frozen=True)
class Number:
    pos: Vector
    width: int
    value: int

    def perimeter(self) -> Iterable[Vector]:
        for y in range(self.pos.y - 1, self.pos.y + 2):
            for x in range(self.pos.x - 1, self.pos.x + self.width + 1):
                if x >= 0 and y >= 0:
                    yield Vector(x, y)

    def contains(self, pos: Vector) -> bool:
        return self.pos.y == pos.y and self.pos.x <= pos.x < (self.pos.x + self.width)


@dataclass(frozen=True)
class Part:
    pos: Vector
    value: str

    def perimeter(self) -> Iterable[Vector]:
        for y in range(self.pos.y - 1, self.pos.y + 2):
            for x in range(self.pos.x - 1, self.pos.x + 2):
                if x >= 0 and y >= 0:
                    yield Vector(x, y)


@dataclass
class Schematic:
    parts: set[Part] = field(default_factory=set)
    numbers: set[Number] = field(default_factory=set)


def parse_input() -> Schematic:
    schematic = Schematic()
    for row, line in enumerate(
        (Path(__file__).parent / "input.txt").read_text().splitlines()
    ):
        for match in re.finditer(r"\d+|[%=@*#+/$&-]", line):
            value = match.group()
            pos = Vector(match.start(), row)
            if value.isnumeric():
                schematic.numbers.add(
                    Number(pos, match.end() - match.start(), int(value))
                )
            else:
                schematic.parts.add(Part(pos, value))
    return schematic


def part_1(schematic: Schematic) -> int:
    part_number_sum = 0
    part_positions = set(part.pos for part in schematic.parts)
    for number in schematic.numbers:
        for position in number.perimeter():
            if position in part_positions:
                part_number_sum += number.value
                break
    return part_number_sum


def part_2(schematic: Schematic) -> int:
    gear_ratio_sum = 0
    possible_gears = [part for part in schematic.parts if part.value == "*"]
    for gear in possible_gears:
        part_numbers = set()
        for position in gear.perimeter():
            for number in schematic.numbers:
                if number.contains(position):
                    part_numbers.add(number)
                    break
        if len(part_numbers) == 2:
            gear_ratio_sum += math.prod(
                part_number.value for part_number in part_numbers
            )
    return gear_ratio_sum


def solve() -> None:
    schematic = parse_input()

    assert part_1(schematic) == 517021

    assert part_2(schematic) == 81296995


if __name__ == "__main__":
    solve()
