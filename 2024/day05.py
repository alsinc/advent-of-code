def get_data(filename):
    rules = []
    updates = []

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if '|' in line:
            nums = [int(n) for n in line.split(sep='|')]
            rules.append(nums)
        elif ',' in line:
            nums = [int(n) for n in line.split(sep=',')]
            updates.append(nums)

    return (rules, updates)

def sort_update(update, rules):
    swaps = True
    while swaps:
        swaps = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                i0 = update.index(rule[0])
                i1 = update.index(rule[1])

                if i0 < i1:
                    pass
                else:
                    #print(f"pre swap update: {update}, swap {i0}, {i1}")
                    swaps = True
                    tmp = update[i0]
                    update[i0] = update[i1]
                    update[i1] = tmp
                    #print(f"post swap update: {update}, swap {i0}, {i1}")

def main():
    part1 = 0
    part2 = 0
    incorrect_updates = []
    (rules, updates) = get_data('day05.input')

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
        else:
            incorrect_updates.append(update)

    for update in incorrect_updates:
        sort_update(update, rules)

        if len(update) % 2 == 1:
            part2 += update[int((len(update) + 1) / 2) - 1]
        else:
            print("OH KNOW")

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
