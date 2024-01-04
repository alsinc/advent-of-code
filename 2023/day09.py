import logging
import sys


def extrapolate_number(numbers, before):
    logging.debug("next_ number: start")
    diffs = []

    last = numbers[0]
    for num in numbers[1:]:
        diff = num - last
        diffs.append(diff)
        last = num

    if diffs.count(0) == len(diffs):
        x = numbers[0]
    else:
        if before:
            x = numbers[0] - extrapolate_number(diffs, before)
        else:
            x = numbers[-1] + extrapolate_number(diffs, before)

    logging.debug("returning: %s", x)
    return x


def part1(report):
    result = 0
    logging.debug("Part 1: Start")
    for history in report:
        next_num = extrapolate_number(history, False)
        logging.debug("Next Number: %s", next_num)
        result += next_num
    print(f"Part 1: {result}")


def part2(report):
    result = 0
    logging.debug("Part 2: Start")
    for history in report:
        next_num = extrapolate_number(history, True)
        logging.debug("Next Number: %s", next_num)
        result += next_num
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
