import sys

def readInput():
    games = {}
    for line in sys.stdin:
        line = line.rstrip()
        [game, picks] = line.split(':')
        gameNo = int(game[5:])
        possible = True
        cubesets = []
        for pick in picks.split(';'):
            cubeset = {}
            for cubes in pick.split(','):
                [quantity, color] = cubes.lstrip().split(' ')
                cubeset[color] = int(quantity)
            cubesets.append(cubeset)
        games[gameNo] = cubesets
    return games

def part1(gamedata):
    limits = {"red": 12, "green": 13, "blue": 14}
    result = 0
    possible = False

    for game in gamedata:
        possible = True
        for cubeset in gamedata[game]:
            for cube in cubeset:
                color = cube
                quantity = cubeset[cube]
                if quantity > limits[color]:
                    possible = False

        if possible:
            result += game
    print(f'Part1: {result}')

def part2(gamedata):
    result = 0

    for game in gamedata:
        quantities = {}
        for cubeset in gamedata[game]:
            for cube in cubeset:
                color = cube
                quantity = cubeset[cube]

                if quantity > quantities.get(color, 0):
                    quantities[color] = quantity
        power = 1
        for q in quantities:
            power *= quantities[q]
        result += power
    print(f'Part2: {result}')

if __name__ == "__main__":
    data = readInput()
    part1(data)
    part2(data)
