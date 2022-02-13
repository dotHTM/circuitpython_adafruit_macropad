from time import monotonic, monotonic_ns
import adafruit_macropad


from Colors import Colors


def timeFn():
    return int(monotonic_ns()/ 1_000)


class MacroPad(adafruit_macropad.MacroPad):
    """docstring for MLCMacroPad"""

    _oldRotation = 0
    encoder_delta = 0
    encoder_direction = 0
    encoder_pressed = False
    encoder_released = False

    _hostConnected = None

    keysPressed = []
    
    _pixelColors = []
    
    new_keys_pressed = []
    
    key_held_start = []
    sleeping = False
    
    idleStart = 0
    def idleReset(self):
        self.idleStart = monotonic()
    def idleDelta(self):
        return monotonic() - self.idleStart
    sleepWait = 5

    def __init__(self, brightness=0.15):
        super(MacroPad, self).__init__()
        self.idleReset()
        self.setLEDBrightness(brightness)
        for i in range(12):
            self._pixelColors.append(Colors.black)
            self.pixels[i] = Colors.black
            self.key_held_start.append(0)
        
    def pixelColor(self, index, color):
        if index < len(self._pixelColors) and index < len(self.pixels):
            if self._pixelColors[index] != color:
                self._pixelColors[index] = color
                self.pixels[index] = color

    def hostConnected(self):
        if self._hostConnected != None:
            return self._hostConnected
        try:
            self.keyboard._keyboard_device
            self._hostConnected = True
        except:
            self._hostConnected = False
        return self.hostConnected()

    def setLEDBrightness(self, newValue):
        if newValue < 0:
            newValue = 0
        if 1 < newValue:
            newValue = 1
        self.pixels.brightness = newValue

    def update(self):
        self.encoder_switch_debounced.update()

        self.sleeping = True if self.sleepWait <= self.idleDelta() else False

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

        while self.keys.events:
            self.idleReset()
            key_event = self.keys.events.get()
            
            if key_event.pressed:
                self.new_keys_pressed = []
                self.key_held_start[key_event.key_number] = timeFn()
                self.new_keys_pressed.append(key_event.key_number)
                self.keysPressed.append(key_event.key_number)
                self.idleTimer = monotonic()
            else:
                self.key_held_start[key_event.key_number] = 0

                while key_event.key_number in self.new_keys_pressed:
                    self.new_keys_pressed.remove(key_event.key_number)
                while key_event.key_number in self.keysPressed:
                    self.keysPressed.remove(key_event.key_number)
    
    def keyHeldTime(self, index):
        if index in self.keysPressed:
            return timeFn() - self.key_held_start[index]
        return 0
    