import time
import math
from rainbowio import colorwheel
import adafruit_macropad


class Notes():
    A = 440
    As = A * 1.06
    B = As * 1.06
    C = B * 1.06
    Cs = C * 1.06
    D = Cs * 1.06
    Ds = D * 1.06
    E = Ds * 1.06
    F = E * 1.06
    Fs = F * 1.06
    G = Fs * 1.06
    Gs = G * 1.06

    base = 1

    w = base
    h = base / 2
    q = base / 4
    e = base / 8
    s = base / 16

    def __init__(self):
        super(Notes, self).__init__()


class MacroPad(adafruit_macropad.MacroPad):
    """docstring for MLCMacroPad"""

    _oldRotation = 0
    encoder_delta = 0
    encoder_direction = 0
    encoder_pressed = False
    encoder_released = True

    def __init__(self, aliveMessage=True):
        super(MacroPad, self).__init__()
        if aliveMessage:
            self.alive()

    def dprint(self, *args):
        for l in args:
            print(l)
        for _ in range(4 - len(args)):
            print()

    def alive(self):
        print("I'm alive!")
        self.singSong()
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
