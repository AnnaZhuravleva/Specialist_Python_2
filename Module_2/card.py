# Начнем с создания карты
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


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
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
        pass


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
# print(...)

# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")