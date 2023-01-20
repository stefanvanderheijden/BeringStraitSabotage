import random


class Deck:
    def __init__(self, type1, amount_type_1, type2, amount_type_2):
        self.type1 = type1
        self.amount_type_1 = amount_type_1
        self.type2 = type2
        self.amount_type_2 = amount_type_2
        self.num_cards = amount_type_1 + amount_type_2

        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for i in range(self.amount_type_1):
            self.cards.append(self.type1)
        for i in range(self.amount_type_2):
            self.cards.append(self.type2)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            drawn_card = self.cards.pop()
            return drawn_card
        else:
            print("Deck empty!")
            return None

    def add_card(self, card):
        self.cards.append(card)

    def add_deck(self, deck):
        for card in deck:
            self.add_card(card)

    def get_deck_height(self):
        return len(self.cards)
