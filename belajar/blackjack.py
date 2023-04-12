import itertools

cards = []
suits = ["hearts", "clovers", "spades", "diamonds"]
suit = suits[2]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
value = 10

print(f"Your card is: {ranks} of {suit}")
for suit, rank in itertools.product(suits, ranks):
    print([suit, rank])
