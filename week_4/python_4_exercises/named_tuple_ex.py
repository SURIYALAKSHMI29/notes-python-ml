from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])
ranks = [str(n) for n in range(2, 11)]
ranks.extend(["J", "Q", "K", "A"])
suits = ["spade", "hearts", "diamonds", "clubs"]


class Deck:

    def __init__(self):
        self.card = [Card(rank, suit) for rank in ranks for suit in suits]


deck = Deck()
card = deck.card[0]  # spade 2

# Accessing
# by index
print(card[1])  # here card -> namedtuple

# by keyname
print(card.rank)

# by getattr()
print(getattr(card, "suit"))


# Conversion
# using _make()
l1 = ["4", "spade"]
t1 = ["A", "hearts"]

print(card._make(l1))
print(card._make(t1))

# using _asdict()
print(card._asdict)

# using **
dic1 = {"rank": "K", "suit": "clubs"}
print(Card(**dic1))

# using *
print(Card(*l1))


# Others
# _fields
print(Card._fields)  # ('rank', 'suit')

# _replace() -> returns a new Card obj
print(card._replace(rank="20"))  # Card(rank='20', suit='spade')
print(card)  # Card(rank='2', suit='spade')

# __getnewargs__()
t2 = card.__getnewargs__()
print(t2)  # ('2', 'spade')
