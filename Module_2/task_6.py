import random
from collections import Counter


class Card:

    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS_RANK = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def __repr__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) > Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANK.index(self.suit) > Card.SUITS_RANK.index(other_card.suit)

    def __lt__(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) < Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANK.index(self.suit) < Card.SUITS_RANK.index(other_card.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        res = list()
        for suit in [Card.HEARTS, Card.DIAMONDS, Card.SPADES, Card.CLUBS]:
            for value in Card.VALUES:
                res.append(Card(value, suit))
        self.cards = res

    def __str__(self):
        to_show = [card.__str__() for card in self.cards]
        return f'deck[{len(self.cards)}]: {", ".join(to_show)}'

    def draw(self, number):
        to_show = self.cards[:number]
        self.cards = self.cards[number:]
        return to_show

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __iter__(self):
        return iter(self.cards)

# task 1

print('task1\n')
deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card1 < card2:
    print(f'карта {card1} меньше {card2}')
else:
    print(f'карта {card1} больше {card2}')


# task 2
deck = Deck()
deck.shuffle()
cards = deck.draw(10)
suits = Counter([card.suit for card in cards]).items()
max_suit = sorted(suits, key=lambda x: x[1])[-1][0]

print('*'* 30)
print('task2\n')
print(f'В колоде оказалось больше всего карт масти {max_suit}')


# task 3
deck = Deck()
deck.shuffle()
card1 = deck.draw(1)[0]
deck.shuffle()
card2 = deck.draw(1)[0]
trials = [card2]
while card2 < card1:
    card2 = deck.draw(1)[0]
    trials.append(card2)

print('*'* 30)
print('task3\n')
print(f'Карта {card2} больше {card1}')
print(f'Первая вытянутая карта - {card1}')
print(f'Остальные вытянутые карты: {", ".join([str(i) for i in trials])}')

# task 4

deck1 = Deck()
deck1.shuffle()

deck2 = Deck()
deck2.shuffle()