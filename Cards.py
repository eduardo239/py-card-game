import random


class Card:
    def __init__(self):
        self.name = ''
        self.attack = ''
        self.defense = ''
        self.deck = []
        self.deck_type = []
        self.deck_type_string = []
        self.deck_attack = []
        self.deck_defense = []

    def get_type(self, deck_list):
        for i in deck_list:
            if i == 1:
                self.deck_type_string.append('water')
            if i == 2:
                self.deck_type_string.append('fire')
            if i == 3:
                self.deck_type_string.append('nature')
        return self.deck_type_string

    def generate_cards(self):
        for k in range(1, 6):
            d = int(random.randint(1, 3))
            self.deck_type.append(d)
        for x in range(1, 6):
            e = int(random.randint(1, 11))
            self.deck_attack.append(e)
        for y in range(1, 6):
            f = int(random.randint(1, 11))
            self.deck_defense.append(f)

        self.get_type(self.deck_type)

        self.deck.append(self.deck_type_string)
        self.deck.append(self.deck_attack)
        self.deck.append(self.deck_defense)
        return self.deck

    def get_cards(self):
        self.generate_cards()
        a = tuple(self.deck_type_string)
        b = tuple(self.deck_attack)
        c = tuple(self.deck_defense)
        z = zip(a, b, c)

        return list(z)


