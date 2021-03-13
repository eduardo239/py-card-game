from cmd.CmdCard import Card


class Player(Card):
    def __init__(self, name):
        super().__init__()
        self.name = name


