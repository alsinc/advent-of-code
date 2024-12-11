def find_words(lines, patterns, word):
    num_words = 0
    for x in range(0, len(lines[0])):
        for y in range(0, len(lines)):
            for w in patterns:
                ok = True
                for c in range(len(w)):
                    newx = x + w[c][0]
                    newy = y + w[c][1]
                    if newx >= len(lines[0]) or newy >= len(lines) or word[c] != lines[newy][newx]:
                        ok = False
                if ok:
                    num_words += 1
    return num_words

def main():
    part1_patterns = [[[0 ,0], [0, 1], [0, 2], [0, 3]],
             [[0 ,0], [1, 0], [2, 0], [3, 0]],
             [[3, 0], [2, 0], [1, 0], [0, 0]],
             [[0, 3], [0, 2], [0, 1], [0 ,0]],
             [[0, 0], [1, 1], [2, 2], [3, 3]],
             [[3, 3], [2, 2], [1, 1], [0 ,0]],
             [[0, 3], [1, 2], [2, 1], [3, 0]],
             [[3, 0], [2, 1], [1, 2], [0, 3]]
             ]
    #AMMSS
    part2_patterns = [[[1, 1], [0, 0], [2, 0], [0, 2], [2, 2]],
                      [[1, 1], [0, 0], [0, 2], [2, 0], [2, 2]],
                      [[1, 1], [2, 0], [2, 2], [0, 0], [0, 2]],
                      [[1, 1], [0, 2], [2, 2], [0, 0], [2, 0]],
                      ]

    with open('day04.input', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    part1 = find_words(lines, part1_patterns, "XMAS")
    part2 = find_words(lines, part2_patterns, "AMMSS")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()

