import storage

from debugHelper import thisDebugPrinter, debugAnounce

thisDebugPrinter.enabled = True
import time
from MacroPad import MacroPad
from Keys import FunctionalKey, LabelKey, TimeKey, TimeHourKey, TimeMinSecKey, ToneKey, BlinkyKey
from Notes import note
from Colors import Colors
from Pages import Page, KeyboardPage


def main():
    macropad = MacroPad(brightness=0.01)
    macropad.appendPage(
        KeyboardPage.fromKeebList(keyboard=macropad.keyboard,
                                  title="1337",
                                  keebList=[["SHIFT",
                                             "F"], 'A', 'Q', 'ESC', 'S', 'W',
                                            'RETURN', 'D', 'E', 'SPACE', 'F', 'R']))
    macropad.appendPage(Page.Pendulum())
    while True:
        macropad.keypadUpdate()


if __name__ == '__main__':
    main()
