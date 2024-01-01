from enum import Enum
import logging
import sys
from collections import Counter

class CardType(Enum):
    FIVE_OF_A_KIND=1
    FOUR_OF_A_KIND=2
    FULL_HOUSE=3
    THREE_OF_A_KIND=4
    TWO_PAIR=5
    ONE_PAIR=6
    HIGH_CARD=7
    UNKNOWN = 0

def get_card_type(hand):
    c = Counter(hand)
    common = c.most_common(5)
    if common[0][1] == 5:
        return CardType.FIVE_OF_A_KIND
    elif common[0][1] == 4:
        return CardType.FOUR_OF_A_KIND
    elif common[0][1] == 3 and common[1][1] == 2:
        return CardType.FULL_HOUSE
    elif common[0][1] == 3:
        return CardType.THREE_OF_A_KIND
    elif common[0][1] == 2 and common[1][1] == 2:
        return CardType.TWO_PAIR
    elif common[0][1] == 2:
        return CardType.ONE_PAIR
    elif len(common) == 5:
        return CardType.HIGH_CARD
    else:
        return CardType.UNKNOWN

def sortkey(value):
    hand = value['hand']
    newhand = hand.translate(str.maketrans("AKQJT98765432", "ABCDEFGHIJKLM"))
    return str(value['card_type'].value) + newhand

def part1(data):
    result = 0
    for hand in data:
        hand['card_type'] = get_card_type(hand['hand'])

    ranked = sorted(data, reverse=True, key=sortkey)
    for r in range(len(ranked)):
        result += ((r+1) * ranked[r]['bid'])
    print(f"Part 1: {result}")

def part2(almanac):
    result = 0
    print(f"Part 2: {result}")

def read_input():
    data = []

    for line in sys.stdin:
        line = line.rstrip()
        items = line.split(' ')
        hand = items[0]
        bid = int(items[1])
        data.append({"hand": hand, "bid": bid})

    return data

def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    data = read_input()
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
