import storage


from debugHelper import thisDebugPrinter, debugAnounce
thisDebugPrinter.enabled = True
import time
from MacroPad import MacroPad
from Keys import FunctionalKey, LabelKey, TimeKey, TimeHourKey, TimeMinSecKey, ToneKey , BlinkyKey
from Notes import note
from Colors import Colors
import Pages


def main():
    macropad = MacroPad()
    macropad.pixels.brightness = 0.425
    # macropad.assignKey(0, LabelKey(desc="time"))
    # macropad.assignKey(1, TimeHourKey(color=Colors.yellow))
    # macropad.assignKey(2, TimeMinSecKey(color=Colors.yellow))
    # macropad.assignKey(3, ToneKey(desc="C", freq= note("C", 4) , color=Colors.green))
    # macropad.assignKey(4, ToneKey(desc="D", freq= note("D", 4) , color=Colors.green))
    # macropad.assignKey(5, ToneKey(desc="E", freq= note("E", 4) , color=Colors.green))
    # macropad.assignKey(6, FunctionalKey( color=Colors.orange))
    
    # macropad.assignKey(9, BlinkyKey(   freq= 4 ,color=Colors.red))
    # macropad.assignKey(10, BlinkyKey(  freq= 2 ,color=Colors.red))
    # macropad.assignKey(11, BlinkyKey(  freq= 1 , color=Colors.red))
    
    
    # for n in range(12):
    
    
    
    macropad.assignPage(Pages.Pendulum())
    
    
    
    
    while True:
        macropad.keypadUpdate()

if __name__ == '__main__':
    main()


