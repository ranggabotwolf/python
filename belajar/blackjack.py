import random
import itertools

cards = []
suits = ["hearts", "clovers", "spades", "diamonds"]
suit = suits[2]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
value = 10

print(f"Your card is: {ranks} of {suit}")
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
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

if rank == "A":
    value = 11
elif rank in ["J", "K", "Q"]:
    value = 10
else:
    value = rank

rank_dict = {"rank": rank, "value": value}
print(rank_dict["rank"], rank_dict["value"])
