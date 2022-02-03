
import Keys
from Colors import Colors, colorwheel

class Page():
    def __init__(self, title="???") -> None:
        self.title = title
        self.keyObjs = []
        for i in range(12):
            self.keyObjs.append(Keys.FunctionalKey(desc="[ ]"))
    
    def assignKey(self, index, key: FunctionalKey):
        if 0 <= index and index < 12:
            self.keyObjs[index] = key




class Pendulum(Page):
    def __init__(self) -> None:
        super().__init__(title="Pendulum")
        for i in range(3):
            for j in range(4):
                n = i + j * 3
                f = (j+1)/4
                p = 0
                if i == 0:
                    p = 135
                elif i == 1:
                    f = f*2
                else:
                    p = -45
                self.assignKey(n, Keys.BlinkyKey( freq= f , phase= p , trigger = 0.5,  color=colorwheel(j*360/4)))

    
    pass