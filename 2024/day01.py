with open('day01.input', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]

a1 = sorted([int(a[0]) for a in lines])
a2 = sorted([int(a[1]) for a in lines])

t1 = 0
t2 = 0

for n in range(len(a1)):
    t1 += abs(a1[n] - a2[n])
    t2 += a2.count(a1[n]) * a1[n]

print(f"Part 1: {t1}")
print(f"Part 2: {t2}")

