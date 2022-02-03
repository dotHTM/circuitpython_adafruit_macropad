import time
import math

from Colors import Colors
from Notes import Notes, note

import time

def noop(*args, **kwargs):
    pass


class FunctionalKey():

    @staticmethod
    def defaultOnUp():
        noop

    @staticmethod
    def defaultOnDown():
        noop

    def __init__(self,
                 onDown=None,
                 onUp=None,
                 desc=None,
                 color=Colors.black) -> None:
        self.keyDown = self.defaultOnUp
        self.keyUp = self.defaultOnDown
        if onDown != None:
            self.keyDown = onDown
        if onUp != None:
            self.keyUp = onUp
        if desc == None :
            desc = "?"
        self.desc = f"{desc:^7}"
        self._color = color

    def onKeyDown(self, fn):

        def inner():
            fn()

        self.keyDown = inner

    def onKeyUp(self, fn):

        def inner():
            fn()

        self.keyUp = inner

    def color(self):
        return self._color

    def __repr__(self) -> str:
        return "<FunctionalKey>"
    
    def label(self):
        return self.desc

class LabelKey(FunctionalKey):
    def __repr__(self) -> str:
        return "<LabelKey>"


class TimeKey(LabelKey):

    def time(self):
        clock = time.monotonic()
        s = int(clock) % (60)
        m = int(clock / 60) % (60)
        h = int(clock / (60**2)) % (24)
        d = int(clock / ((60**2) * 24))
        return (d, h, m, s)

    def __repr__(self) -> str:
        return "<TimeKey>"
        
    def label(self):
        (d, h, m, s) = self.time()
        return f"{d:02d}:{h:02d}:{m:02d}{s:02d}"


class TimeHourKey(TimeKey):

    def label(self):
        (d, h, m, s) = self.time()
        return f"{d:02d}:{h:02d}:"


class TimeMinSecKey(TimeKey):

    def label(self):
        (d, h, m, s) = self.time()
        return f":{m:02d}:{s:02d}"


class ToneKey(FunctionalKey):
    
    def __init__(self, *args, freq=None, note=None, octave=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.freq = freq
        
    def __repr__(self) -> str:
        return f"<ToneKey({','.join([str(self.desc),str(self.freq)])})>"
        
    
class BlinkyKey(FunctionalKey):
    
    def __init__(self, *args, phase=0, freq = 0.5, trigger = 0,  **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.phase = phase
        if freq == 0:
            freq = 1/100
        self.freq = freq
        self.trigger = trigger
    
    def color(self):
        x = time.monotonic()
        n = math.sin(
            ( x * 2* self.freq + self.phase / 180  ) * math.pi  ) 
        
        # print( x , n, self.freq)
        if self.trigger < n:
            return super().color()
        return Colors.black