import time
from Colors import Colors, colorwheel, hexValue
from TitledGridDisplay import TitledGridDisplay
from debugHelper import thisDebugPrinter
from debugHelper.Analyzer import LoopAnalyzer, mean

thisDebugPrinter.enabled = True

from MacroPad import MacroPad

from debugHelper import debugAnounce


class App():

    def __init__(self, macropad):
        self.macropad = macropad
        self.grid = TitledGridDisplay(self.macropad)
        print(f"{self} Start")

    def update(self):
        self.grid.update()
        self.grid.setTitle("Time Held")
        for k in self.macropad.keysPressed:
            pass
        for k in range(12):
            color = colorwheel(
                self.macropad.keyHeldTime(k) * 36,
                1 - min(0.99,
                        self.macropad.keyHeldTime(k) / 30),
                min(1,
                    self.macropad.keyHeldTime(k) / 10),
            )
            self.macropad.pixelColor(k, color)
            self.grid.setLabel(k, f"{self.macropad.keyHeldTime(k):5.04}")

    def __repr__(self) -> str:
        return "<App()>"


@debugAnounce
def main():
    macropad = MacroPad()
    app = App(macropad)
    la = LoopAnalyzer()
    while True:
        time.sleep(0.0001)
        la.update()
        macropad.update()
        app.update()
        print(f"""
================================
    t : {time.monotonic()}
  zzz : {macropad.sleeping}
   zt : {macropad.idleDelta()}
    d : {la.delta}

""")


if __name__ == '__main__':
    main()
