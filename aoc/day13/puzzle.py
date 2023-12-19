from pathlib import Path


def parse_input() -> list[list[str]]:
    patterns = []
    for pattern in (Path(__file__).parent / "input.txt").read_text().split("\n\n"):
        patterns.append(pattern.splitlines())
    return patterns


def transpose(pattern: list[str]) -> list[str]:
    cols = ["" for _ in pattern[0]]
    for row in pattern:
        for x, char in enumerate(row):
            cols[x] += char
    return cols


def part_1(patterns: list[list[str]]) -> int:
    summarized = 0

    for pattern in patterns:
        for y in range((len(pattern))):
            behind = list(reversed(pattern[:y]))
            ahead = pattern[y:]
            if behind and ahead:
                smallest = min(len(behind), len(ahead))
                if behind[:smallest] == ahead[:smallest]:
                    summarized += len(behind) * 100

        transposed = transpose(pattern)
        for y in range(len(transposed)):
            behind = list(reversed(transposed[:y]))
            ahead = transposed[y:]
            if behind and ahead:
                smallest = min(len(behind), len(ahead))
                if behind[:smallest] == ahead[:smallest]:
                    summarized += len(behind)

    return summarized


def solve() -> None:
    patterns = parse_input()

    assert part_1(patterns) == 29846


if __name__ == "__main__":
    solve()
