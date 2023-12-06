import re
from pathlib import Path


def parse_input() -> str:
    games = []
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        _, details = line.split(": ")
        turns = details.split("; ")
        game = []
        for turn in turns:
            cubes = turn.split(", ")
            game.append([])
            for cube in cubes:
                match = re.match('(\d+) (blue|green|red)', cube)
                amount = match.group(1)
                color = match.group(2)
                game[-1].append((int(amount), color))
        games.append(game)
    return games

def part_1(games):

    summed = 0
    for game_id, game in enumerate(games, 1):
        possible = True
        for turn in game:
            for amount, cube in turn:
                if cube == 'blue' and amount > 14:
                    possible = False
                elif cube == 'red' and amount > 12:
                    possible = False
                elif cube == 'green' and amount > 13:
                    possible = False
        if possible:
            summed += game_id
    assert summed == 2283

def part_2(games):
    summed = 0
    for game_id, game in enumerate(games, 1):
        min_red = 0
        min_blue = 0
        min_green = 0
        for turn in game:
            for amount, cube in turn:
                if cube == 'red':
                    min_red = max(min_red, amount)
                elif cube == 'green':
                    min_green = max(min_green, amount)
                elif cube == 'blue':
                    min_blue = max(min_blue, amount)
        summed += min_red * min_blue * min_green
    assert summed == 78669

def solve() -> None:
    games = parse_input()

    part_1(games)
    part_2(games)


if __name__ == "__main__":
    solve()
