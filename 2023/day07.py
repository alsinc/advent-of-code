from collections import Counter
from enum import Enum
import logging
import sys


class CardType(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7
    UNKNOWN = 0


def get_card_type(hand, joker_rule):
    c = Counter(hand)

    common = c.most_common(5)
    jokers = 0
    if joker_rule:
        jokers = c.get("J", 0)
        if jokers == 5:
            return CardType.FIVE_OF_A_KIND
        elif jokers > 0:
            common.remove(("J", jokers))

    if common[0][1] + jokers == 5:
        return CardType.FIVE_OF_A_KIND
    elif common[0][1] + jokers == 4:
        return CardType.FOUR_OF_A_KIND
    elif common[0][1] + jokers == 3 and common[1][1] == 2:
        return CardType.FULL_HOUSE
    elif common[0][1] + jokers == 3:
        return CardType.THREE_OF_A_KIND
    elif common[0][1] == 2 and common[1][1] == 2:
        return CardType.TWO_PAIR
    elif common[0][1] + jokers == 2:
        return CardType.ONE_PAIR
    elif len(common) == 5:
        return CardType.HIGH_CARD
    else:
        return CardType.UNKNOWN


def sortkey(value):
    hand = value["hand"]
    newhand = hand.translate(str.maketrans("AKQJT98765432", "ABCDEFGHIJKLM"))
    return str(value["card_type"].value) + newhand


def sortkey_joker_low(value):
    hand = value["hand"]
    newhand = hand.translate(str.maketrans("AKQT98765432J", "ABCDEFGHIJKLM"))
    return str(value["card_type"].value) + newhand


def calc_total_winnings(data, joker_rule):
    result = 0
    for hand in data:
        hand["card_type"] = get_card_type(hand["hand"], joker_rule)

    ranked = sorted(
        data, reverse=True, key=sortkey_joker_low if joker_rule else sortkey
    )
    for r in range(len(ranked)):
        result += (r + 1) * ranked[r]["bid"]

    return result


def part1(data):
    result = calc_total_winnings(data, False)
    print(f"Part 1: {result}")


def part2(data):
    result = calc_total_winnings(data, True)
    print(f"Part 2: {result}")


def read_input():
    data = []

    for line in sys.stdin:
        line = line.rstrip()
        items = line.split(" ")
        hand = items[0]
        bid = int(items[1])
        data.append({"hand": hand, "bid": bid})

    return data


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    data = read_input()
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
