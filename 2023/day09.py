import logging
import sys


def next_number(numbers):
    logging.debug("next_ number: start")
    diffs = []

    last = numbers[0]
    for num in numbers[1:]:
        diff = num - last
        diffs.append(diff)
        last = num

    diffs_sorted = sorted(diffs)
    if diffs_sorted[0] == diffs_sorted[-1] and diffs_sorted[0] == 0:
        x = numbers[0]
    else:
        x = numbers[-1] + next_number(diffs)

    logging.debug("returning: %s", x)
    return x


def part1(report):
    result = 0
    for history in report:
        next_num = next_number(history)
        logging.debug("Next Number: %s", next_num)
        result += next_num
    print(f"Part 1: {result}")


def part2(report):
    result = 0
    print(f"Part 2: {result}")


def read_input():
    report = []

    for line in sys.stdin:
        line = line.rstrip()
        history = [int(x) for x in line.split(" ")]
        report.append(history)
    return report


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    report = read_input()
    part1(report)
    part2(report)


if __name__ == "__main__":
    main()
