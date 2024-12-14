part1 = 0
part2 = 0
param1 = 0
param2 = 0
enabled = True


def dummyhook(p):
    pass


def enable(p):
    global enabled
    enabled = True


def disable(p):
    global enabled
    enabled = False


def startparams(p):
    global param1, param2
    param1 = 0
    param2 = 0


def firstparam(p):
    global param1
    param1 = param1 * 10 + (ord(p) - ord("0"))


def secondparam(p):
    global param2
    param2 = param2 * 10 + (ord(p) - ord("0"))


def gotboth(p):
    global part1, part2
    part1 = part1 + param1 * param2
    if enabled:
        part2 = part2 + param1 * param2


states = {
    "START": {
        "m": {"newstate": "GOTM", "hook": dummyhook},
        "d": {"newstate": "GOTD", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTM": {
        "u": {"newstate": "GOTMU", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTMU": {
        "l": {"newstate": "GOTMUL", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTMUL": {
        "(": {"newstate": "GOTMUL(", "hook": startparams},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTMUL(": {
        "0": {"newstate": "GM1ST", "hook": firstparam},
        "1": {"newstate": "GM1ST", "hook": firstparam},
        "2": {"newstate": "GM1ST", "hook": firstparam},
        "3": {"newstate": "GM1ST", "hook": firstparam},
        "4": {"newstate": "GM1ST", "hook": firstparam},
        "5": {"newstate": "GM1ST", "hook": firstparam},
        "6": {"newstate": "GM1ST", "hook": firstparam},
        "7": {"newstate": "GM1ST", "hook": firstparam},
        "8": {"newstate": "GM1ST", "hook": firstparam},
        "9": {"newstate": "GM1ST", "hook": firstparam},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GM1ST": {
        "0": {"newstate": "GM1ST", "hook": firstparam},
        "1": {"newstate": "GM1ST", "hook": firstparam},
        "2": {"newstate": "GM1ST", "hook": firstparam},
        "3": {"newstate": "GM1ST", "hook": firstparam},
        "4": {"newstate": "GM1ST", "hook": firstparam},
        "5": {"newstate": "GM1ST", "hook": firstparam},
        "6": {"newstate": "GM1ST", "hook": firstparam},
        "7": {"newstate": "GM1ST", "hook": firstparam},
        "8": {"newstate": "GM1ST", "hook": firstparam},
        "9": {"newstate": "GM1ST", "hook": firstparam},
        ",": {"newstate": "GMCOMMA", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GMCOMMA": {
        "0": {"newstate": "GM2ND", "hook": secondparam},
        "1": {"newstate": "GM2ND", "hook": secondparam},
        "2": {"newstate": "GM2ND", "hook": secondparam},
        "3": {"newstate": "GM2ND", "hook": secondparam},
        "4": {"newstate": "GM2ND", "hook": secondparam},
        "5": {"newstate": "GM2ND", "hook": secondparam},
        "6": {"newstate": "GM2ND", "hook": secondparam},
        "7": {"newstate": "GM2ND", "hook": secondparam},
        "8": {"newstate": "GM2ND", "hook": secondparam},
        "9": {"newstate": "GM2ND", "hook": secondparam},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GM2ND": {
        "0": {"newstate": "GM2ND", "hook": secondparam},
        "1": {"newstate": "GM2ND", "hook": secondparam},
        "2": {"newstate": "GM2ND", "hook": secondparam},
        "3": {"newstate": "GM2ND", "hook": secondparam},
        "4": {"newstate": "GM2ND", "hook": secondparam},
        "5": {"newstate": "GM2ND", "hook": secondparam},
        "6": {"newstate": "GM2ND", "hook": secondparam},
        "7": {"newstate": "GM2ND", "hook": secondparam},
        "8": {"newstate": "GM2ND", "hook": secondparam},
        "9": {"newstate": "GM2ND", "hook": secondparam},
        ")": {"newstate": "START", "hook": gotboth},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTD": {
        "o": {"newstate": "GOTDO", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTDO": {
        "(": {"newstate": "GOTDO(", "hook": dummyhook},
        "n": {"newstate": "GOTDON", "hook": dummyhook},
    },
    "GOTDO(": {
        ")": {"newstate": "START", "hook": enable},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTDON": {
        "'": {"newstate": "GOTDON'", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTDON'": {
        "t": {"newstate": "GOTDON'T", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTDON'T": {
        "(": {"newstate": "GOTDON'T(", "hook": dummyhook},
        "**": {"newstate": "START", "hook": dummyhook},
    },
    "GOTDON'T(": {
        ")": {"newstate": "START", "hook": disable},
        "**": {"newstate": "START", "hook": dummyhook},
    },
}


def main():
    with open("day03.input", "r") as f:
        state = "START"
        while byte := f.read(1):
            if byte in states[state]:
                states[state][byte]["hook"](byte)
                state = states[state][byte]["newstate"]
            else:
                if "**" in states[state]:
                    states[state]["**"]["hook"](byte)
                    state = states[state]["**"]["newstate"]
                else:
                    print("NO DEFAULT TRANSITION")
                    break

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
