import random


class Card:
    suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
              'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {'Hearts': '\u2665',
                 'Diamonds': '\u2666',
                 'Spades': '\u2663',
                 'Clubs': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        res = list()
        for value in Card.values:
            for suit in Card.suits:
                res.append(Card(value, suit))
        return res

    def show(self):
        to_show = [card.to_str() for card in self.cards]
        return f'deck[{len(self.cards)}]: {", ".join(to_show)}'

    def draw(self, number):
        to_show = self.cards[:number]
        self.cards = self.cards[number:]
        return to_show

    def shuffle(self):
        self.cards = random.shuffle(self.cards)
        

