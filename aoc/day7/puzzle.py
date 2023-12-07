from __future__ import annotations
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

    @staticmethod
    def from_raw_hand(hand: str) -> Type:
        counts = Counter(hand)
        hand_type = Type.HIGH_CARD
        for count in counts.values():
            if count == 5:
                return Type.FIVE_OF_A_KIND
            elif count == 4:
                return Type.FOUR_OF_A_KIND
            elif count == 3:
                if hand_type == Type.ONE_PAIR:
                    hand_type = Type.FULL_HOUSE
                else:
                    hand_type = Type.THREE_OF_A_KIND
            elif count == 2:
                if hand_type == Type.ONE_PAIR:
                    hand_type = Type.TWO_PAIR
                elif hand_type == Type.THREE_OF_A_KIND:
                    hand_type = Type.FULL_HOUSE
                else:
                    hand_type = Type.ONE_PAIR
        return hand_type


CARD_RANKINGS = {c: i for i, c in enumerate("AKQJT98765432")}


@dataclass
class Hand:
    raw: str
    bid: int
    hand_type: Type = field(init=False)

    def __post_init__(self):
        self.hand_type = Type.from_raw_hand(self.raw)

    def apply_joker(self):
        counts = Counter(self.raw)
        if (joker_count := counts.get("J")) and joker_count != 5:
            best_joker = next(
                card
                for card, _ in sorted(
                    counts.items(), key=lambda count: count[1], reverse=True
                )
                if card != "J"
            )
            self.hand_type = Type.from_raw_hand(self.raw.replace("J", best_joker))

    def __lt__(self, other):
        if self.hand_type.value != other.hand_type.value:
            return self.hand_type.value < other.hand_type.value
        for a, b in zip(self.raw, other.raw):
            if a != b:
                return CARD_RANKINGS[a] > CARD_RANKINGS[b]


def parse_input() -> Iterable[Hand]:
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        hand, bid = line.split(" ")
        yield Hand(hand, int(bid))


def part_1(hands: list[Hand]) -> int:
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


def part_2(hands: list[Hand]) -> int:
    global CARD_RANKINGS
    CARD_RANKINGS = {c: i for i, c in enumerate("AKQT98765432J")}
    for hand in hands:
        hand.apply_joker()
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


def solve() -> None:
    hands = list(parse_input())

    assert part_1(hands) == 246912307

    assert part_2(hands) == 246894760


if __name__ == "__main__":
    solve()
