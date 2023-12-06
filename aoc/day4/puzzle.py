import re
import collections
from pathlib import Path
from typing import Iterable

Card = tuple[list[int], list[int]]


def parse_input() -> Iterable[Card]:
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        if match := re.match(r"Card\s+\d+: (.+) \| (.+)", line):
            win = [int(num) for num in match.group(1).split(" ") if num]
            own = [int(num) for num in match.group(2).split(" ") if num]
            yield (win, own)


def part_1(cards: list[Card]) -> int:
    return sum(
        2 ** (matching - 1)
        for win, own in cards
        if (matching := len(set(win) & set(own))) > 0
    )


def part_2(cards: list[Card]) -> int:
    copies = collections.defaultdict(lambda: 1)
    for card, (win, own) in enumerate(cards):
        matching = len(set(win) & set(own))
        multiplier = copies[card]
        for offset in range(matching):
            copies[card + offset + 1] += multiplier
    return sum(copies.values())


def solve() -> None:
    cards = list(parse_input())

    assert part_1(cards) == 23235

    assert part_2(cards) == 5920640


if __name__ == "__main__":
    solve()
