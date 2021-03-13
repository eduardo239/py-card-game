import random
CARD_TYPE = [
    'water', 'fire', 'ice'
]


class Card:
    def __init__(self):
        self.deck = []

    def generate_deck(self):
        for i in range(1, 6):
            dk = []

            for k in range(len(CARD_TYPE) - 1):
                dk.append(random.randint(1, 10))

            for m in range(1, 2):
                ek = random.randint(1, len(CARD_TYPE))
                dk.append(self.get_card_type(ek))
            self.deck.append(dk)
        return self.deck

    def get_card_type(self, el):
        if el == 1: return CARD_TYPE[0]
        if el == 2: return CARD_TYPE[1]
        if el == 3: return CARD_TYPE[2]

    def get_deck(self):
        self.generate_deck()
        return self.deck
