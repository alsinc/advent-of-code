import sys

def readdata():
    lines = []
    for line in sys.stdin:
        line = line.rstrip()
        lines.append(line)
    return lines

def neighbours(data, r, c):
    n = []
    if r > 0:
        if c > 0:
            n.append(data[r-1][c-1])
        n.append(data[r-1][c])

        if c < (len(data[r])-1):
            n.append(data[r-1][c+1])
    if c > 0:
        n.append(data[r][c-1])
    if c < (len(data[r])-1):
        n.append(data[r][c+1])

    if r < (len(data)-1):
        if c > 0:
            n.append(data[r+1][c-1])
        n.append(data[r+1][c])
        if c < (len(data[r])-1):
            n.append(data[r+1][c+1])

    return n


def part1(data):
    result = 0
    for r in range(len(data)):
        value = 0
        isPartNumber = False
        for c in range(len(data[r])):
            char = data[r][c]
            if char.isdigit():
                n = neighbours(data, r, c)
                for neigh in n:
                    if neigh != '.' and not neigh.isdigit():
                        isPartNumber = True

                value = value * 10 + int(char)

            if not char.isdigit() or c == (len(data[r])-1):
                if value:
                    if isPartNumber:
                        result += value
                    value = 0
                    isPartNumber = False
    print(f'Part 1: {result}')

def part2(data):
    for r in range(len(data)):
        value = 0
        isPartNumber = False
        for c in range(len(data[r])):
            char = data[r][c]
            if char == '*':
                n = neighbours(data, r, c)
                #print(n)

def main():
    data = readdata()
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
