import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal():
    return random.choice(cards)

def calc(list):
    return sum(list)


def ace_check(deck):
    if sum(deck) > 21 and 11 in deck:       
        ace = deck.index[11]
        deck[ace] = 1
        return calc(deck)

def black_jack(total, deck):
    if total == 21:
        if 11 in deck:
            return 0


