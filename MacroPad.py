import time
from rainbowio import colorwheel
import adafruit_macropad

import displayio
import terminalio
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_display_text import bitmap_label as label
from Colors import Colors
from Keys import FunctionalKey, LabelKey, ToneKey, Notes
import math

from Pages import Page



def mean(thisList):
    if len(thisList) != 0:
        return sum(thisList) / len(thisList)
    return None

def now():
    return time.monotonic()

def now_ms():
    return int(time.monotonic_ns() / 1000)


class MacroPad(adafruit_macropad.MacroPad):
    """docstring for MLCMacroPad"""
    
    blankPage = Page()
    pageStack = []
    currentPage = None

    refreshSleep = 0.01
    lastTime = now_ms()

    _oldRotation = 0
    encoder_delta = 0
    encoder_direction = 0
    encoder_pressed = False
    encoder_released = False

    _hostConnected = None

    idleStart = time.monotonic()
    idleThreshold = 30
    idleSleeping = False

    def resetIdle(self):
        self.idleStart = time.monotonic()
        self.idleSleeping = False

    def idleTime(self):
        delta = time.monotonic() - self.idleStart
        return delta

    # keyObjs = []
    # for i in range(12):
    #     keyObjs.append(FunctionalKey(desc=f""))

    keyStack = []
    main_group = None

    toneStack = []
    playingTone = None
    
    

    def toneUpdate(self):
        newToneStack = list(
            filter(lambda e: isinstance(e, ToneKey), self.keyStack))

        self.toneChanged = False
        if self.toneStack != newToneStack:
            self.toneChanged = True
            self.toneStack = newToneStack

        self.topToneStack = None
        if 0 < len(self.toneStack):
            self.topToneStack = self.toneStack[-1]

    def __init__(self, aliveMessage=True, brightness= 0.010):
        super(MacroPad, self).__init__()
        if len(self.pageStack) == 0:
            self.appendPage(self.blankPage)
        self.setLEDBrightness( brightness )
        if aliveMessage:
            self.alive()

    def hostConnected(self):
        if self._hostConnected != None:
            return self._hostConnected
        try:
            self.keyboard._keyboard_device
            self._hostConnected = True
        except Exception as e:
            self._hostConnected = False
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

    # def assignKey(self, index, key: FunctionalKey):
    #     if 0 <= index and index < 12:
    #         self.keyObjs[index] = key

    

    def assignPage(self, newPage: Page):
        currentPage = newPage
        
        
    def appendPage(self, newPage: Page):
        while self.blankPage in self.pageStack:
            self.pageStack.remove(self.blankPage)
        self.pageStack.append(newPage)

    def setupGridDisplay(self):
        self.main_group = displayio.Group()
        self.display.show(self.main_group)
        self.title = label.Label(
            y=4,
            font=terminalio.FONT,
            color=0x0,
            text=f"{'Hello!':^22}",
            background_color=0xFFFFFF,
        )
        self.layout = GridLayout(x=0,
                                 y=10,
                                 width=128,
                                 height=54,
                                 grid_size=(3, 4),
                                 cell_padding=1)
        self.labels = []
        for _ in range(12):
            self.labels.append(label.Label(terminalio.FONT, text="[ ]"))

        for index in range(12):
            x = index % 3
            y = index // 3
            self.layout.add_content(self.labels[index],
                                    grid_position=(x, y),
                                    cell_size=(1, 1))

        self.main_group.append(self.title)
        self.main_group.append(self.layout)

    lagHist = []
    peakLag = 0

    def analizeLag(self):
        time.sleep(self.refreshSleep)
        now_now = now_ms()
        delta = now_now - self.lastTime
        self.lagHist.append(delta)
        window = 10
        if window < len(self.lagHist):
            del self.lagHist[0]
        print(
            f"max={max(self.lagHist):<,.}\tmin={min(self.lagHist):<,.}\tavg{window}={int(mean(self.lagHist)):<,.}\t{delta=:<,.}"
        )
        self.lastTime = now_now

    def evalKeyDown(self, thisKey):
        self.keyStack.append(thisKey)
        if not self.idleSleeping:
            thisKey.keyDown()

    def evalKeyUp(self, thisKey):
        while thisKey in self.keyStack:
            self.keyStack.remove(thisKey)
            if not self.idleSleeping:
                thisKey.keyUp()

    sleepLEDBrightness = 0.01
    wakeLEDBrightness = 0.5

    def setLEDBrightness(self, newValue):
        if newValue < 0:
            newValue = 0
        if 1 < newValue:
            newValue = 1
        self.wakeLEDBrightness = newValue
        self.pixels.brightness = newValue

    def update(self):
        # self.analizeLag()

        self.encoder_switch_debounced.update()

        oldPressed = self.encoder_pressed
        self.encoder_pressed = self.encoder_switch_debounced.pressed

        self.encoder_pressed_event = self.encoder_pressed and not oldPressed

        oldReleased = self.encoder_released
        self.encoder_released = self.encoder_switch_debounced.released

        self.encoder_released_event = self.encoder_released and not oldReleased

        current_encoder = self.encoder
        self.encoder_delta = self._oldRotation - current_encoder
        if 0 < self.encoder_delta:
            self.encoder_direction = 1
        elif self.encoder_delta < 0:
            self.encoder_direction = -1
        else:
            self.encoder_direction = 0
        self._oldRotation = current_encoder

    currentTitle = "Hello!"
    mode = "key"
    
    keyPages = []
    menuPages = []

    def keypadUpdate(self):
        self.update()
        
        if self.currentPage == None:
            self.currentPage = self.pageStack[0]

        for condition in [self.encoder_direction != 0, self.encoder_pressed, self.keys.events, self.keyStack]:
            if condition:
                self.resetIdle()

        if self.main_group == None:
            self.setupGridDisplay()

        # update the Title bar
        titleColor = 0x0
        titleBackgroundColor = 0xFFFFFF
        newTitleText = self.currentPage.title
        if self.idleSleeping:
            newTitleText = ""
            if int(now()) % 2 == 0:
                newTitleText = "zzz"
            titleColor = 0xFFFFFF
            titleBackgroundColor = 0x0

        newTitleText = f"{newTitleText:^21}"

        if self.title.text != newTitleText:
            self.title.text = newTitleText
        if self.title.color != titleColor:
            self.title.color = titleColor
        if self.title.background_color != titleBackgroundColor:
            self.title.background_color = titleBackgroundColor

        # update the per-key data (labels, active, pixel values, etc)
        lc = 0
        for thisKey in self.currentPage.keyObjs:

            l = self.labels[lc]
            newLabelText = thisKey.label()
            if l.text != newLabelText:
                l.text = newLabelText

            color = 0xFFFFFF
            background_color = 0x0
            if thisKey in self.keyStack:
                if not isinstance(thisKey, LabelKey):
                    color = 0x0
                    background_color = 0xFFFFFF

            if self.idleSleeping:
                color = 0x0
                background_color = 0x0

            if l.color != color:
                l.color = color
            if l.background_color != background_color:
                l.background_color = background_color

            p = self.pixels[lc]
            newColor = thisKey.color()
            if p != newColor:
                self.pixels[lc] = newColor
            lc += 1

        if self.idleThreshold < self.idleTime():
            self.idleSleeping = True
            self.pixels.brightness = self.sleepLEDBrightness
        else:
            if self.pixels.brightness != self.wakeLEDBrightness:
                self.pixels.brightness = self.wakeLEDBrightness

        if self.mode == "menu":

            if self.encoder_pressed:
                self.mode = "key"
                print("entering key mode")
            else:
                pass

        elif self.mode == "key":

            if self.encoder_pressed:
                self.mode = "menu"
                print("entering menu mode")
            else:
                while self.keys.events:
                    key_event = self.keys.events.get()
                    kNumber = key_event.key_number
                    thisKey = self.currentPage.keyObjs[kNumber]
                    if key_event.pressed:
                        # Add pressed key to the stack
                        self.evalKeyDown(thisKey)
                    else:
                        # Remove released key from the stack
                        self.evalKeyUp(thisKey)

                ## Evaluate musical keys
                self.toneUpdate()
                if self.toneChanged and self.playingTone != self.topToneStack:
                    self.stop_tone()
                    self.playingTone = None
                    if self.topToneStack != None:
                        self.start_tone(self.topToneStack.freq)
                        self.playingTone = self.topToneStack
