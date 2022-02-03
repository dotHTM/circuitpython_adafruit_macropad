import time
import math

from Colors import Colors


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
                 desc='<key>',
                 color=Colors.black) -> None:
        self.keyDown = self.defaultOnUp
        self.keyUp = self.defaultOnDown
        if onDown != None:
            self.keyDown = onDown
        if onUp != None:
            self.keyUp = onUp
        self.desc = desc
        self.color = color

    def onKeyDown(self, fn):

        def inner():
            fn()

        self.keyDown = inner

    def onKeyUp(self, fn):

        def inner():
            fn()

        self.keyUp = inner

    def getColor(self):
        return self.color

    def __repr__(self) -> str:
        return self.desc


class LabelKey(FunctionalKey):
    pass


class TimeKey(LabelKey):

    def time(self):
        clock = time.monotonic()
        s = int(clock) % (60)
        m = int(clock / 60) % (60)
        h = int(clock / (60**2)) % (24)
        d = int(clock / ((60**2) * 24))
        return (d, h, m, s)

    def __repr__(self) -> str:
        (d, h, m, s) = self.time()
        return f"{h:02d}{m:02d}{s:02d}"


class TimeHourKey(TimeKey):

    def __repr__(self) -> str:
        (d, h, m, s) = self.time()
        return f"{d:02d}:{h:02d}:"


class TimeMinSecKey(TimeKey):

    def __repr__(self) -> str:
        (d, h, m, s) = self.time()
        return f":{m:02d}:{s:02d}"


class ToneStack():
    stack = []

    def append(self, element):
        self.stack.append(element)

    def remove(self, element):
        while element in self.stack:
            self.stack.remove(element)

    def top(self):
        if 0 < len(self.stack):
            return self.stack[-1]
        return None


class ToneKey(FunctionalKey):

    def __init__(self, *args, macropad=None, freq=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if macropad == None:
            print("undefined parent macropad")
            exit()
        self.macropad = macropad
        if freq == None:
            freq = 440
        self.freq = freq
        self.onKeyDown(lambda: self.macropad.start_tone(self.freq) )
        self.onKeyUp( self.macropad.stop_tone )
        


class Notes():
    semitone = 1.0595

    A = 440
    As = A * semitone
    B = As * semitone
    ## backsolve C, then the rest arise similarly
    C = B * semitone / 2
    Cs = C * semitone
    D = Cs * semitone
    Ds = D * semitone
    E = Ds * semitone
    F = E * semitone
    Fs = F * semitone
    G = Fs * semitone
    Gs = G * semitone

    base = 1

    w = base
    h = base / 2
    q = base / 4
    e = base / 8
    s = base / 16

    noteStack = []

    def __init__(self):
        super(Notes, self).__init__()

    def note(n, o):
        pass
