import storage


from debugHelper import thisDebugPrinter, debugAnounce
thisDebugPrinter.enabled = True
import time
from MacroPad import MacroPad
from Keys import FunctionalKey, LabelKey, TimeKey, TimeHourKey, TimeMinSecKey, ToneKey
from Colors import Colors

def main():
    macropad = MacroPad()
    macropad.pixels.brightness = 0.125
    macropad.assignKey(0, LabelKey(desc="time"))
    macropad.assignKey(1, TimeHourKey(color=Colors.orange))
    macropad.assignKey(2, TimeMinSecKey(color=Colors.orange))
    macropad.assignKey(3, ToneKey(macropad = macropad, freq= 220 , color=Colors.green))
    macropad.assignKey(4, ToneKey(macropad = macropad, freq= 440 , color=Colors.green))
    macropad.assignKey(5, ToneKey(macropad = macropad, freq= 880 , color=Colors.green))
    while True:
        time.sleep(0.01)
        macropad.keypadUpdate()

if __name__ == '__main__':
    main()


