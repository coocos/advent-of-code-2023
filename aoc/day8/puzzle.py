import re
import math
from pathlib import Path
from dataclasses import dataclass


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


def part_2(instructions: str, graph: Graph) -> int:
    step = 0
    first_time_at_z = {}
    ghost_nodes = [node for node in graph.values() if node.name.endswith("A")]
    while len(first_time_at_z) != len(ghost_nodes):
        for ghost, node in enumerate(ghost_nodes):
            if instructions[step % len(instructions)] == "L":
                ghost_nodes[ghost] = graph[node.left]
            else:
                ghost_nodes[ghost] = graph[node.right]
            if node.name.endswith("Z") and ghost not in first_time_at_z:
                first_time_at_z[ghost] = step
        step += 1
    return math.lcm(*first_time_at_z.values())


def solve() -> None:
    instructions, graph = parse_input()

    assert part_1(instructions, graph) == 17263

    assert part_2(instructions, graph) == 14631604759649


if __name__ == "__main__":
    solve()
