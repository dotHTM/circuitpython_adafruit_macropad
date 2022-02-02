import time
import math
from rainbowio import colorwheel
import adafruit_macropad


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


class MacroPad(adafruit_macropad.MacroPad):
    """docstring for MLCMacroPad"""
    
    

    _oldRotation = 0
    encoder_delta = 0
    encoder_direction = 0
    encoder_pressed = False
    encoder_released = True
    
    _hostConnected = None

    def __init__(self, aliveMessage=True):
        super(MacroPad, self).__init__()
        if aliveMessage:
            self.alive()

    def hostConnected(self):
        if self._hostConnected != None:
            return self._hostConnected
        
        try:
            self.keyboard._keyboard_device
            self._hostConnected =  True
        except Exception as e:
            self._hostConnected =  False
        return self.hostConnected()

    def dprint(self, *args):
        for l in args:
            print(l)
        for _ in range(4 - len(args)):
            print()

    def alive(self):
        print("I'm alive!")
        # self.singSong()
        if self.pixels != None:
            for i in range(12):
                self.pixels[i] = colorwheel(int(i / 12 * 360))
                time.sleep(0.025)
            # time.sleep(0.5)
            for i in range(12):
                self.pixels[i] = 0
                time.sleep(0.025)
        self.dprint()

    def singSong(self):
        song = [
            (Notes.C, Notes.e),
            (Notes.D, Notes.e),
            (Notes.G, Notes.e),
            (Notes.A, Notes.e),
            (Notes.C, Notes.e),
            (Notes.B, Notes.e),
        ]
        for note in song:
            (freq, duration) = note
            self.play_tone(freq, duration)

    def update(self):
        self.encoder_switch_debounced.update()
        self.encoder_pressed = self.encoder_switch_debounced.pressed
        self.encoder_released = self.encoder_switch_debounced.released
        current_encoder = self.encoder
        self.encoder_delta = self._oldRotation - current_encoder
        if 0 < self.encoder_delta:
            self.encoder_direction = 1
        elif self.encoder_delta < 0:
            self.encoder_direction = -1
        else:
            self.encoder_direction = 0
        self._oldRotation = current_encoder

    def values(self):
        data = {
            "encoder": self.encoder,
            "encoder_delta": self.encoder_delta,
            "encoder_direction": self.encoder_direction,
            "encoder_pressed": self.encoder_pressed,
            "encoder_released": self.encoder_released,
        }

        return data
        pass


thisMacropad = MacroPad()
