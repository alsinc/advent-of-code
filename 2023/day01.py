f = open("day01.input", "r", newline='\n')

result = 0
for l in f:
    first = last = 0
    for c in l:
        if c >= '0' and c<='9':
            if not first:
                first = int(c)
            last = int(c)
    calibration = first * 10 + last
    result = result + calibration

print(f"Calibration sum: {result}")