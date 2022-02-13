
from MacroPad import MacroPad
from TitledGridDisplay import TitledGridDisplay


class Button():
    def __init__(self, onDown, onUp, label, color):
        super(Button, self).__init__()
        self.onDown = onDown
        self.onUp = onUp
        self.label = label
        self.color = color

class Application():
    def __init__(self, macropad: MacroPad ):
        self.macropad = macropad
