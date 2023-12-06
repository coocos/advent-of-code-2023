from pathlib import Path

name_to_digit = {
    'one': '1',
    'eno': '1',
    'two': '2',
    'owt': '2',
    'three': '3',
    'eerht': '3',
    'four': '4',
    'ruof': '4',
    'five': '5',
    'evif': '5',
    'six': '6',
    'xis': '6',
    'seven': '7',
    'neves': '7',
    'eight': '8',
    'thgie': '8',
    'nine': '9',
    'enin': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

def parse_input() -> list[str]:
    return (Path(__file__).parent / "input.txt").read_text().splitlines()


def solve() -> None:

    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    total = 0
    for line in parse_input():
        first_digit = '-1'
        first_digit_position = len(line) + 1
        for digit in digits:
            position = line.find(digit)
            if position != -1 and position < first_digit_position:
                first_digit = digit
                first_digit_position = position

        reversed_line = line[::-1]
        last_digit = '-1'
        last_digit_position = len(reversed_line) + 1
        for digit in [d[::-1] for d in digits]:
            position = reversed_line.find(digit)
            if position != -1 and position < last_digit_position:
                last_digit = digit
                last_digit_position = position
        line_sum = int(f'{name_to_digit[first_digit]}{name_to_digit[last_digit]}')
        total += line_sum

    assert total == 54676


if __name__ == "__main__":
    solve()