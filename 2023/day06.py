import logging
import sys

def count_wins(time, distance):
    result = 0
    for t in range(time+1):
        d = -t*t + t*time

        if d > distance:
            result += 1
    return result


def part1(races):
    result = 1
    (times, distances) = races
    for race in zip(times, distances):
        logging.debug("Race: Time; %s, Distance: %s", race[0], race[1])
        count = count_wins(race[0], race[1])
        result *= count
        logging.debug("Race can be one in %s ways", count)
    print(f"Part 1: {result}")

def part2(races):
    (times, distances) = races
    time =0
    distance = 0
    for t in times:
        time = time * 10**len(str(t)) + t

    for d in distances:
        distance = distance * 10**len(str(d)) + d

    logging.debug("Time: %s", time)
    logging.debug("Distance: %s", distance)

    result = count_wins(time, distance)
    print(f"Part 2: {result}")

def read_input():
    times = sys.stdin.readline()[5:].split(' ')
    distances = sys.stdin.readline()[9:].split(' ')

    times = [int(x) for x in times if len(x) > 0]
    distances = [int(x) for x in distances if len(x) > 0]

    logging.debug("times: %s", times)
    logging.debug("distances: %s", distances)
    return (times, distances)

def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    races = read_input()
    part1(races)
    part2(races)

if __name__ == '__main__':
    main()
