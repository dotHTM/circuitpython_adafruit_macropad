
from Colors import Colors, colorwheel
import Keys

class Page():
    
    def __init__(self, title="Page Title") -> None:
        self.title = title
        self.keyObjs = []
        for i in range(12):
            self.keyObjs.append(Keys.FunctionalKey(desc="[ ]"))
    
    def assignKey(self, index, key: FunctionalKey):
        if 0 <= index and index < 12:
            self.keyObjs[index] = key
    
    @staticmethod
    def Pendulum():
        thisPage = Page(title="Pendulum")
        for j in range(4):
            for i in range(3):
                n = i + j * 3
                f = (j+1)/4
                p = 0
                if i == 0:
                    p = 135
                elif i == 1:
                    f = f*2
                else:
                    p = -45
                thisPage.assignKey(n, Keys.BlinkyKey( freq= f , phase= p , trigger = 0.5,  color=colorwheel(j*360/4)))
        return thisPage

class KeyboardPage(Page):
    def __init__(self, keyboard, title="KB Page") -> None:
        super().__init__(title)
        self.keyboard = keyboard
    
    def assignKeeb(self, index, keyList, **kwargs):
        thisKey = Keys.FunctionalKey.HoldKeeb(self.keyboard, keyList, **kwargs)
        self.assignKey(index=index, key=thisKey)
    
    @staticmethod
    def fromKeebList(keyboard, title, keebList):
        thisPage = KeyboardPage(title=title, keyboard=keyboard)
        lc = 0
        for kb in keebList:
            thisPage.assignKeeb(lc, kb)
            lc += 1
        return thisPage    


###  