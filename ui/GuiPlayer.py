from ui import GuiCard


class GuiPlayer(GuiCard):
    def __init__(self, name):
        super().__init__()
        self.name = name


