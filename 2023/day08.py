import logging
import sys


def part1(directions, network):
    result = 0
    dir = 0

    node = "AAA"

    while node != "ZZZ":
        d = directions[dir]
        logging.debug(d)

        logging.debug(network[node])

        if d == "L":
            node = network[node][0]
        else:
            node = network[node][1]

        result += 1
        logging.debug("Node: %s", node)

        dir += 1
        if dir == len(directions):
            dir = 0

    print(f"Part 1: {result}")


def part2(directions, network):
    result = 0
    print(f"Part 2: {result}")


def read_input():
    network = dict()

    directions = sys.stdin.readline().rstrip()
    logging.debug("dir: %s", directions)

    for line in sys.stdin:
        line = line.rstrip()
        if len(line) > 0:
            node = line[:3]
            left = line[7:10]
            right = line[12:15]
            network[node] = (left, right)

    return directions, network


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    directions, network = read_input()
    part1(directions, network)
    part2(directions, network)


if __name__ == "__main__":
    main()
