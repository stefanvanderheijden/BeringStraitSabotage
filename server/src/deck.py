import random


class Deck:
    def __init__(self, type1, type2, num_cards):
        self.type1 = type1
        self.type2 = type2
        self.num_cards = num_cards
        self.cards = []
        self.create_deck()
        self.shuffle()
        self.drawn_cards = []

    def create_deck(self):
        for i in range(self.num_cards):
            self.cards.append(self.type1)
        for i in range(self.num_cards):
            self.cards.append(self.type2)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            drawn_card = self.cards.pop()
            self.drawn_cards.append(drawn_card)
            return drawn_card
        else:
            return None

    def add_card(self, card):
        self.cards.append(card)

    def get_num_cards(self):
        return len(self.cards)

    def get_drawn_cards(self):
        return self.drawn_cards
