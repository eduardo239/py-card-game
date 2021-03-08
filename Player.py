from Cards import Card


class Player(Card):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.deck = []
        self.score = 0
        self.win = 0
        self.lose = 0

    def get_player_info(self):
        return self.name
