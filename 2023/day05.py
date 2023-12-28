import logging
import sys

class Almanac():
    def __init__(self, seeds, maps):
        self.seeds = seeds
        self.maps = maps

class Range():
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.end = start + length - 1

class MappingRange():
    def __init__(self, dest_range_start, source_range_start, range_length):
        self.destination = Range(dest_range_start, range_length)
        self.source = Range(source_range_start, range_length)

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

    logging.debug(f"Using mapping: {mapping}")
    ranges = maps[mapping]

    for map_range in ranges:
        logging.debug(f"map: {map_range.source.start} - {map_range.source.end}")
        mapped = True
        while mapped:
            mapped = False
            for vi in range(len(values)):
                vr = values[vi]
                logging.debug(f"value: {vr.start} - {vr.end} len {vr.length}")
                if (vr.start >= map_range.source.start and vr.start <= map_range.source.end) or \
                   (vr.end >= map_range.source.start and vr.end <= map_range.source.end):

                    new_end = 0
                    if vr.end > map_range.source.end:
                        new_end = map_range.source.end
                    else:
                        new_end = vr.end

                    new_start = 0
                    if vr.start < map_range.source.start:
                        new_start = map_range.source.start
                    else:
                        new_start = vr.start

                    new_length = new_end - new_start + 1

                    new_range = Range(new_start - map_range.source.start + map_range.destination.start, new_length)
                    logging.debug(f"adding new range {new_range.start} - {new_range.end} = len {new_range.length}")
                    new_values.append(new_range)

                    if new_length == vr.length:
                        del values[vi]
                    else:
                        if new_start > vr.start:
                            vr.end = new_start - 1
                        else:
                            vr.start = vr.start + new_length
                        vr.length = vr.end - vr.start + 1
                    mapped = True
                    break

    if len(values) > 0:
        for v in values:
            new_values.append(v)

    return destination_category, new_values

def dump_values(values):
    for v in values:
        logging.debug(f"{v.start} - {v.end} len {v.length}")

def do_mapping(source_category, destination_category, almanac, values):
    category = source_category
    while category != destination_category:
        logging.debug("----- Before mapping --------")
        dump_values(values)
        logging.debug("-----------------------------")
        category, values = map_values(almanac.maps, category, values)
        logging.debug("----- After mapping --------")
        dump_values(values)
        logging.debug("----------------------------")

    return values

def part1(almanac):
    result = 0

    values = [Range(s, 1) for s in almanac.seeds]
    values = do_mapping("seed", "location", almanac, values)

    result = min([v.start for v in values])
    print(f"Part 1: {result}")

def part2(almanac):
    result = 0

    s = len(almanac.seeds)
    seeds = []
    for sp in range(int(s/2)):
        seed_range_start = almanac.seeds[sp*2]
        seed_range_len = almanac.seeds[sp*2+1]
        seeds.append(Range(seed_range_start, seed_range_len))

    values = do_mapping("seed", "location", almanac, seeds)

    result = min([v.start for v in values])

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
            range = MappingRange(int(dest_start), int(source_start), int(range_length))
            maps[map_name].append(range)

    return Almanac(seeds=seeds, maps=maps)

def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    almanac = read_input()
    part1(almanac)
    part2(almanac)

if __name__ == '__main__':
    main()
