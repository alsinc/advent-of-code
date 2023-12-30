import logging
import math
import sys

def count_wins(time, distance):
    t1 = (-time + (time**2 - 4 * distance)**0.5) / -2
    t2 = (-time - (time**2 - 4 * distance)**0.5) / -2

    res = math.floor(t2) - math.ceil(t1) + 1
    if math.trunc(t1) == t1:
        res -=1

    if math.trunc(t2) == t2:
        res -=1

    logging.debug("t1 = %s, t2 = %s, res = %s", t1, t2, res)

    return res

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
