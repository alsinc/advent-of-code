import sys
class Almanac():
    def __init__(self, seeds, maps):
        self.seeds = seeds
        self.maps = maps

class Range():
    def __init__(self, dest_range_start, source_range_start, range_length):
        self.dest_range_start = dest_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

def map_values(maps, category, values):
    mapping = ""
    new_values = []
    for m in maps:
        p = m.find('-to-')
        source_category = m[:p]
        destination_category = m[p+4:]
        if category == source_category:
            mapping = m
            break

    ranges = maps[mapping]
    for v in values:
        new_value = -1
        for r in ranges:
            if v >= r.source_range_start and v < (r.source_range_start + r.range_length):
                new_value = v - r.source_range_start + r.dest_range_start
                break
        if new_value == -1:
            new_value = v
        new_values.append(new_value)

    return destination_category, new_values

def part1(almanac):
    result = 0
    category = "seed"

    values = almanac.seeds
    while category != "location":
        category, values = map_values(almanac.maps, category, values)

    result = min(values)
    print(f"Part 1: {result}")

def part2(almanac):
    result = 0
    print(f"Part 2: {result}")

def read_input():
    maps = {}
    map_name = ""

    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith("seeds: "):
            seeds = [int(x) for x in line[7:].split(" ")]
        elif line.endswith(" map:"):
            map_name = line.split(" ")[0]
            maps[map_name] = []
        elif len(line) > 0:
            [dest_start, source_start, range_length] = line.split(' ')
            range = Range(int(dest_start), int(source_start), int(range_length))
            maps[map_name].append(range)

    return Almanac(seeds=seeds, maps=maps)

def main():
    almanac = read_input()
    part1(almanac)
    part2(almanac)

if __name__ == '__main__':
    main()
