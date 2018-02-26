

class PokerCard:

    valid_suits = ("HEARTS", "SPADES", "CLUBS", "DIAMONDS")
    valid_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    def __init__(self, value=None, suit=None):

        if 0 < value < 14:
            self.value = value
        else:
            self.value = None
        if suit in PokerCard.valid_suits:
            self.suit = suit
        else:
            self.suit = None
        self.representation = None
        if self.suit and self.value:
            self._find_representation()

    def _find_representation(self):
        self.representation = "["
        if self.value == 1:
            self.representation += "A "
        elif self.value == 11:
            self.representation += "J "
        elif self.value == 12:
            self.representation += "Q "
        elif self.value == 13:
            self.representation += "K "
        elif self.value == 10:
            self.representation += "10"
        else:
            self.representation += str(self.value) + " "

        self.representation += self.suit[0] + "]"

    def __str__(self):
        return self.representation


class Deck:

    def __init__(self, card_class):
        self.cards = []
        for suit in card_class.valid_suits:
            for value in card_class.valid_values:
                self.cards.append(card_class(value, suit))


deck = Deck(PokerCard)
for card in deck.cards:
    print(str(card))
