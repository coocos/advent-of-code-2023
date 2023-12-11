import collections
import itertools
from pathlib import Path


def parse_input() -> list[tuple[int, int]]:
    galaxies = []
    for y, row in enumerate(
        (Path(__file__).parent / "input.txt").read_text().splitlines()
    ):
        for x, col in enumerate(row):
            if col == "#":
                galaxies.append((int(x), int(y)))
    return galaxies


def distances(galaxies: list[tuple[int, int]], multiplier: int = 1) -> int:
    mutated = list(galaxies)

    max_x = max(pos[0] for pos in galaxies)
    max_y = max(pos[1] for pos in galaxies)

    galaxies_at_x = collections.defaultdict(list)
    galaxies_at_y = collections.defaultdict(list)
    for galaxy, position in enumerate(galaxies):
        galaxies_at_x[position[0]].append(galaxy)
        galaxies_at_y[position[1]].append(galaxy)

    x_expansion = 0
    for x in range(0, max_x + 1):
        if not galaxies_at_x[x]:
            x_expansion += multiplier
            continue
        for galaxy in galaxies_at_x[x]:
            mutated[galaxy] = (mutated[galaxy][0] + x_expansion, mutated[galaxy][1])

    y_expansion = 0
    for y in range(0, max_y + 1):
        if not galaxies_at_y[y]:
            y_expansion += multiplier
            continue
        for galaxy in galaxies_at_y[y]:
            mutated[galaxy] = (mutated[galaxy][0], mutated[galaxy][1] + y_expansion)

    return sum(
        abs(a[0] - b[0]) + abs(a[1] - b[1])
        for a, b in itertools.combinations(mutated, 2)
    )


def solve() -> None:
    galaxies = parse_input()

    # Part 1
    assert distances(galaxies) == 9312968

    # Part 2
    assert distances(galaxies, 999_999) == 597714117556


if __name__ == "__main__":
    solve()
