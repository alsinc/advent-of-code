dirs = [
    ("<", (-1, 0)),
    ("^", (0, -1)),
    (">", (1, 0)),
    ("v", (0, 1)),
]


def get_data(filename):
    with open(filename, "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines


def main():
    part1 = 0
    part2 = 0
    direction_index = -1
    direction = ()
    row_pos = 0
    col_pos = 0
    visited = {}

    data = get_data("day06.input")
    for row in range(len(data)):
        for col in range(len(data[row])):
            if "<>^v".find(data[row][col]) > -1:
                for d in range(len(dirs)):
                    if dirs[d][0] == data[row][col]:
                        direction_index = d
                        direction = dirs[d][1]
                        row_pos = row
                        col_pos = col
                break

    if direction_index > -1:
        while True:
            # print(f"{row_pos} {col_pos}")
            visited[(row_pos, col_pos)] = 1

            new_col_pos = col_pos + direction[0]
            new_row_pos = row_pos + direction[1]

            if new_col_pos < 0 or new_col_pos > len(data[0]):
                # print("Reached left or right side")
                break

            if new_row_pos < 0 or new_row_pos > len(data):
                # print("Reached top or bottom")
                break

            if data[new_row_pos][new_col_pos] == "#":
                # print("Hit a wall")
                direction_index = (direction_index + 1) % 4
                direction = dirs[direction_index][1]
            else:
                row_pos = new_row_pos
                col_pos = new_col_pos

    part1 = len(visited)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
