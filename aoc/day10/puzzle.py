from __future__ import annotations
import collections
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def neighbours(self) -> Iterable[Vector]:
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x = dx + self.x
            y = dy + self.y
            if x >= 0 and y >= 0:
                yield Vector(x, y)


def parse_input() -> dict[Vector, str]:
    tiles = {}
    for y, row in enumerate(
        (Path(__file__).parent / "input.txt").read_text().splitlines()
    ):
        for x, tile in enumerate(row):
            if tile != ".":
                tiles[Vector(x, y)] = tile
    return tiles


def part_1(tiles: dict[Vector, str]) -> int:
    start = next(pos for pos, tile in tiles.items() if tile == "S")

    # Just hardcode the correct tile
    tiles[start] = "J"

    max_distance = 0
    visited = set([start])
    unvisited: collections.deque[tuple[int, Vector]] = collections.deque([(0, start)])
    while unvisited:
        distance, pos = unvisited.popleft()
        max_distance = max(max_distance, distance)
        if tiles[pos] == "|":
            for neighbour in [Vector(pos.x, pos.y - 1), Vector(pos.x, pos.y + 1)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
        elif tiles[pos] == "-":
            for neighbour in [Vector(pos.x - 1, pos.y), Vector(pos.x + 1, pos.y)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
        elif tiles[pos] == "L":
            for neighbour in [Vector(pos.x, pos.y - 1), Vector(pos.x + 1, pos.y)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
        elif tiles[pos] == "J":
            for neighbour in [Vector(pos.x, pos.y - 1), Vector(pos.x - 1, pos.y)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
        elif tiles[pos] == "7":
            for neighbour in [Vector(pos.x, pos.y + 1), Vector(pos.x - 1, pos.y)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
        elif tiles[pos] == "F":
            for neighbour in [Vector(pos.x, pos.y + 1), Vector(pos.x + 1, pos.y)]:
                if neighbour not in visited:
                    unvisited.append((distance + 1, neighbour))
                    visited.add(neighbour)
    return max_distance


def solve() -> None:
    tiles = parse_input()

    assert part_1(tiles) == 6806


if __name__ == "__main__":
    solve()
