def line_is_safe(line):
    n = 1
    diff = int(line[1]) - int(line[0])
    direction = 1 if diff > 0 else -1

    while (n < len(line) and (diff * direction) >= 1 and (diff * direction) <= 3):
        diff = int(line[n]) - int(line[n-1])
        n += 1

    if (n == len(line) and diff * direction >= 1 and diff * direction <= 3):
        return True
    else:
        return False

def main():
    with open('day02.input', 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]

    part1 = 0
    part2 = 0
    for line in lines:
        if line_is_safe(line):
            part1 += 1

        for n in range(len(line)):
            t = line[n]
            del line[n]
            if line_is_safe(line):
                part2 += 1
                break
            line.insert(n, t)


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
