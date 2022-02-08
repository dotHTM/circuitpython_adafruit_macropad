
import time
from Colors import Colors
from TitledGridDisplay import TitledGridDisplay
from debugHelper import thisDebugPrinter
thisDebugPrinter.enabled = True

from MacroPad import MacroPad

from debugHelper import debugAnounce
@debugAnounce
def main():
    macropad = MacroPad()
    grid = TitledGridDisplay(macropad.display)
    while True:
        time.sleep(0.001)
        macropad.update()
        
        grid.title.set("Hello there")
        for k in range(12):
            grid.labelTexts[k].set(f"k {k}")
        
        for k in macropad.keysPressed:
            grid.labelTexts[k].set(time.monotonic())
        
        


if __name__ == '__main__':
    main()
