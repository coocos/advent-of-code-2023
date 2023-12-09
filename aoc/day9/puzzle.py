import itertools
from pathlib import Path


def parse_input() -> list[list[int]]:
    histories = []
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        histories.append([int(num) for num in line.split(" ")])
    return histories


def differences(history: list[int]) -> list[list[int]]:
    differences = [history]
    while any(num != 0 for num in differences[-1]):
        last_seq = differences[-1]
        next_seq = [b - a for a, b in itertools.pairwise(last_seq)]
        differences.append(next_seq)
    return differences


def part_1(histories: list[list[int]]) -> int:
    extrapolated_sum = 0
    for history in histories:
        prev = 0
        for diff in reversed(differences(history)):
            diff.append(diff[-1] + prev)
            prev = diff[-1]
        extrapolated_sum += prev
    return extrapolated_sum


def part_2(histories: list[list[int]]) -> int:
    extrapolated_sum = 0
    for history in histories:
        prev = 0
        for diff in reversed(differences(history)):
            diff.insert(0, diff[0] - prev)
            prev = diff[0]
        extrapolated_sum += prev
    return extrapolated_sum


def solve() -> None:
    histories = parse_input()

    assert part_1(histories) == 1696140818

    assert part_2(histories) == 1152


if __name__ == "__main__":
    solve()
