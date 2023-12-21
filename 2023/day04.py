import sys

class Card:
    def __init__(self, number, wins, ours):
        self.cardnumber = number
        self.winningnumbers = wins
        self.ournumbers = ours
        self.quantity = 1

def parseline(line):
    colon = line.find(':')
    numbers = line[colon+1:]
    pipe = numbers.find('|')
    winningnums = numbers[:pipe]
    ournums = numbers[pipe+1:]

    card = int(line[colon-3:colon])
    wins = [int(x) for x in winningnums.split(' ') if x != '']
    ours = [int(x) for x in ournums.split(' ') if x != '']
    return Card(card, wins, ours)

def readdata():
    lines = []
    for line in sys.stdin:
        lines.append(parseline(line.rstrip()))
    return lines

def part1(cards):
    totalpoints = 0
    for card in cards:
        winners = [x for x in card.winningnumbers if card.ournumbers.count(x)>0]
        if len(winners) > 0:
            points = 2**(len(winners)-1)
            totalpoints += points

    print(f"Part 1: {totalpoints}")

def part2(cards):
    for c in range(len(cards)):
        winners = [x for x in cards[c].winningnumbers if cards[c].ournumbers.count(x)>0]
        for w in range(c+1, c+len(winners)+1):
            cards[w].quantity += cards[c].quantity

    result = 0
    for card in cards:
        result += card.quantity

    print(f"Part 2: {result}")


if __name__ == "__main__":
    data = readdata()
    part1(data)
    part2(data)
