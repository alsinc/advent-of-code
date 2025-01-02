def get_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = []
    for line in lines:
        data.append(
            {
                "target": int(line.split(sep=":")[0]),
                "numbers": [int(x) for x in line.split(sep=":")[1].split()],
            }
        )

    return data


def check_equation(numbers, target, index, total, operators):
    if index == len(numbers):
        return False

    for op in operators:
        newtot = op(total, numbers[index])
        if newtot == target and (index + 1) == len(numbers):
            return True
        else:
            if check_equation(numbers, target, index + 1, newtot, operators):
                return True


def main():
    part1 = 0
    part2 = 0

    operatorsp1 = [lambda tot, x: tot + x, lambda tot, x: tot * x]
    operatorsp2 = [
        lambda tot, x: tot + x,
        lambda tot, x: tot * x,
        lambda tot, x: int(str(tot) + str(x)),
    ]

    data = get_data("day07.input")
    for equation in data:
        nums = equation["numbers"]
        target = equation["target"]
        if check_equation(nums, target, 0, 0, operatorsp1):
            print(f"{nums} {target}")
            part1 += target

        if check_equation(nums, target, 0, 0, operatorsp2):
            print(f"{nums} {target}")
            part2 += target

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
