from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterable


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


card_rankings = {c: i for i, c in enumerate("AKQJT98765432")}


@dataclass
class Hand:
    raw: str
    bid: int
    hand_type: Type = field(init=False)

    def __post_init__(self):
        self.hand_type = Type.HIGH_CARD
        counts = Counter(self.raw)
        for count in counts.values():
            if count == 5:
                self.hand_type = Type.FIVE_OF_A_KIND
                break
            elif count == 4:
                self.hand_type = Type.FOUR_OF_A_KIND
                break
            elif count == 3:
                if self.hand_type == Type.ONE_PAIR:
                    self.hand_type = Type.FULL_HOUSE
                else:
                    self.hand_type = Type.THREE_OF_A_KIND
            elif count == 2:
                if self.hand_type == Type.ONE_PAIR:
                    self.hand_type = Type.TWO_PAIR
                elif self.hand_type == Type.THREE_OF_A_KIND:
                    self.hand_type = Type.FULL_HOUSE
                else:
                    self.hand_type = Type.ONE_PAIR

    def __lt__(self, other):
        if self.hand_type.value != other.hand_type.value:
            return self.hand_type.value < other.hand_type.value
        for a, b in zip(self.raw, other.raw):
            if a != b:
                return card_rankings[a] > card_rankings[b]


def parse_input() -> Iterable[Hand]:
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        hand, bid = line.split(" ")
        yield Hand(hand, int(bid))


def part_1(hands: list[Hand]) -> int:
    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), 1))


def solve() -> None:
    hands = list(parse_input())

    assert part_1(hands) == 246912307


if __name__ == "__main__":
    solve()
