import random
import itertools


cards = []
suits = ["hearts", "clovers", "spades", "diamonds"]
ranks = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
]

print(f"Your card is: {ranks} of {suits}")
print("\n")
# April, 14 2023
for suit, rank in itertools.product(suits, ranks):
    cards.append([suit, rank])


def shuffle():
    random.shuffle(cards)


def deal(number):
    card_dealt = []
    for x in range(number):
        card = cards.pop()
        card_dealt.append(card)
    return card_dealt


shuffle()
card = deal(1)[0]
print(card[1]["value"])
