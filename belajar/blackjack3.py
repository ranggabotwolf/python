import random
import itertools


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank["rank"] + " of " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
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
        # for suit in suits:
        # for rank in ranks:
        # self.cards.append([suit, rank])
        # code diatas bisa diganti dengan code baris 27-28
        self.cards.extend(
            [suit, rank] for suit, rank in itertools.product(suits, ranks)
        )

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        card_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                card_dealt.append(card)
        return card_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print("\n")
print(deck2.cards)