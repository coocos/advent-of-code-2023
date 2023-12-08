from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Node:
    name: str
    left: str
    right: str


Graph = dict[str, Node]


def parse_input() -> tuple[str, Graph]:
    instructions, nodes = (
        (Path(__file__).parent / "input.txt").read_text().split("\n\n")
    )
    graph: Graph = {}
    for node in nodes.splitlines():
        if match := re.match(r"(\w+) = \((\w+), (\w+)\)", node):
            node, left, right = match.groups()
            graph[node] = Node(node, left, right)
    return instructions, graph


def part_1(instructions: str, graph: Graph) -> int:
    step = 0
    current = graph["AAA"]
    while current.name != "ZZZ":
        if instructions[step % len(instructions)] == "L":
            current = graph[current.left]
        else:
            current = graph[current.right]
        step += 1
    return step


def solve() -> None:
    instructions, graph = parse_input()

    assert part_1(instructions, graph) == 17263


if __name__ == "__main__":
    solve()
