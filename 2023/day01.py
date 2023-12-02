p1digits = {"0": 1, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

p2digits = {"0": 0,
    "1": 1, "one": 1,
    "2": 2, "two": 2,
    "3": 3, "three": 3,
    "4": 4, "four": 4,
    "5": 5, "five": 5,
    "6": 6, "six": 6,
    "7": 7, "seven": 7,
    "8": 8, "eight": 8,
    "9": 9, "nine": 9,
}

def getCalibration(dict):
    f = open("day01.input", "r", newline='\n')
    result = 0

    for l in f:
        bestfirst = 99999
        bestfirstvalue = 0
        bestlast = -1
        bestlastvalue = 0

        for key in dict:
            first = l.find(key)
            if first != -1 and first < bestfirst:
                bestfirst = first
                bestfirstvalue = dict[key]

            last = l.rfind(key)
            if last != -1 and last > bestlast:
                bestlast = last
                bestlastvalue = dict[key]

        calibration = bestfirstvalue * 10 + bestlastvalue
        result = result + calibration
    f.close()
    return result

p1 = getCalibration(p1digits)
p2 = getCalibration(p2digits)
print(f"Part 1: {p1}\nPart 2: {p2}")
