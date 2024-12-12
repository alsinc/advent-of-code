def main():
    rules = []
    updates = []
    part1 = 0

    with open('day05.input', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if '|' in line:
            nums = [int(n) for n in line.split(sep='|')]
            rules.append(nums)
        elif ',' in line:
            nums = [int(n) for n in line.split(sep=',')]
            updates.append(nums)

    for update in updates:
        ok = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    ok = False
        if ok:
            if len(update) % 2 == 1:
                part1 += update[int((len(update) + 1) / 2) - 1]
            else:
                print("OH KNOW")

    print(f"Part 1: {part1}")

if __name__ == "__main__":
    main()
