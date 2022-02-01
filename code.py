import time
from colorsys import hsv_to_rgb
from MacroPad import MacroPad

macropad = MacroPad()

from adafruit_hid.keycode import Keycode as kc


def cc(key):

    def inner():
        macropad.consumer_control.send(key)

    return inner


def noop(*args, **kwargs):
    pass


class KeyPressObj():
    keyDown = noop
    keyUp = noop

    def __init__(self, keycodeList: list[kc]):

        def onDown():
            for k in keycodeList:
                macropad.keyboard.press(k)

        def onUp():
            for k in reversed(keycodeList):
                macropad.keyboard.release(k)

        self.keyDown = onDown
        self.keyUp = onUp

    def __repr__(self) -> str:
        return "<KeyPressObj>"


class FnKeyMap():

    def __init__(self, arg):
        super(FnKeyMap, self).__init__()
        self.keyDown = noop
        self.keyUp = noop
        if isinstance(arg, KeyPressObj):
            self.keyDown = arg.keyDown
            self.keyUp = arg.keyUp

    def onKeyDown(self, fn):
        if callable(fn):
            self.keyDown = fn

    def onKeyUp(self, fn):
        if callable(fn):
            self.keyUp = fn


def keyPress(*keycodeList):
    return FnKeyMap(KeyPressObj(keycodeList))


# thisKey = keyPress(kc.SHIFT, kc.THREE)

# time.sleep(1)

# for _ in range(4):
#     thisKey.keyDown()
#     time.sleep(.1)
#     thisKey.keyUp()
#     time.sleep(.1)

# time.sleep(2)


class SpecialKeys():
    BRIGHTNESS_DECREMENT = cc(
        macropad.ConsumerControlCode.BRIGHTNESS_DECREMENT)
    BRIGHTNESS_INCREMENT = cc(
        macropad.ConsumerControlCode.BRIGHTNESS_INCREMENT)

    RECORD = cc(macropad.ConsumerControlCode.RECORD)

    REWIND = cc(macropad.ConsumerControlCode.REWIND)
    PLAY_PAUSE = cc(macropad.ConsumerControlCode.PLAY_PAUSE)
    FAST_FORWARD = cc(macropad.ConsumerControlCode.FAST_FORWARD)

    STOP = cc(macropad.ConsumerControlCode.STOP)
    SCAN_NEXT_TRACK = cc(macropad.ConsumerControlCode.SCAN_NEXT_TRACK)
    SCAN_PREVIOUS_TRACK = cc(macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK)

    MUTE = cc(macropad.ConsumerControlCode.MUTE)
    VOLUME_DECREMENT = cc(macropad.ConsumerControlCode.VOLUME_DECREMENT)
    VOLUME_INCREMENT = cc(macropad.ConsumerControlCode.VOLUME_INCREMENT)

    EJECT = cc(macropad.ConsumerControlCode.EJECT)


def colorwheel(theta, saturation=1, value=1):
    return hsv_to_rgb(theta / 360, saturation, value)


def mixColors(a, b):
    c = []
    for i in range(3):
        c.append(int((a[i] + b[i]) / 2))
    return tuple(c)


class Colors():
    white = (255, 255, 255)
    lightGrey = (196, 196, 196)
    grey = (128, 128, 128)
    darkGrey = (64, 64, 64)
    lightBlack = (10, 10, 10)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    yellow = (255, 255, 0)
    orange = (255, 128, 0)


def consumer_control_key(key_int):
    return key_int


mappings = [
    {
        "title":
        "Media",
        "keys": [
            SpecialKeys.MUTE,
            SpecialKeys.VOLUME_DECREMENT,
            SpecialKeys.VOLUME_INCREMENT,
            keyPress(kc.ESCAPE),
            keyPress(kc.UP_ARROW),
            keyPress(
                kc.CONTROL,
                kc.SHIFT,
                kc.OPTION,
                kc.COMMAND,
                kc.H,
            ),
            keyPress(kc.LEFT_ARROW),
            keyPress(kc.DOWN_ARROW),
            keyPress(kc.RIGHT_ARROW),
            SpecialKeys.SCAN_PREVIOUS_TRACK,
            SpecialKeys.PLAY_PAUSE,
            SpecialKeys.SCAN_NEXT_TRACK,
        ],
        "pixels": [
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            Colors.orange,
            Colors.lightBlack,
            Colors.yellow,
            Colors.lightBlack,
            Colors.lightBlack,
            Colors.lightBlack,
            colorwheel(0, 0.75, 0.5),
            colorwheel(120, 0.75, 0.5),
            colorwheel(240, 0.75, 0.5),
        ]
    },
    {
        "title":
        "Numbers",
        "keys": [
            keyPress(kc.KEYPAD_ONE),
            keyPress(kc.KEYPAD_TWO),
            keyPress(kc.KEYPAD_THREE),
            keyPress(kc.KEYPAD_FOUR),
            keyPress(kc.KEYPAD_FIVE),
            keyPress(kc.KEYPAD_SIX),
            keyPress(kc.KEYPAD_SEVEN),
            keyPress(kc.KEYPAD_EIGHT),
            keyPress(kc.KEYPAD_NINE),
            keyPress(kc.KEYPAD_PERIOD),
            keyPress(kc.KEYPAD_ZERO),
            keyPress(kc.KEYPAD_ENTER),
        ],
        "pixels": [
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.orange,
            Colors.white,
            Colors.red,
        ],
    },
    {
        "title":
        "F-Keys",
        "keys": [
            keyPress(kc.F1),
            keyPress(kc.F2),
            keyPress(kc.F3),
            keyPress(kc.F4),
            keyPress(kc.F5),
            keyPress(kc.F6),
            keyPress(kc.F7),
            keyPress(kc.F8),
            keyPress(kc.F9),
            keyPress(kc.F10),
            keyPress(kc.F11),
            keyPress(kc.F12),
        ],
        "baseColor":
        Colors.darkGrey,
    },
    {
        "title":
        "F-Upper",
        "keys": [
            keyPress(kc.F13),
            keyPress(kc.F14),
            keyPress(kc.F15),
            keyPress(kc.F16),
            keyPress(kc.F17),
            keyPress(kc.F18),
            keyPress(kc.F19),
            keyPress(kc.F20),
            keyPress(kc.F21),
            keyPress(kc.F22),
            keyPress(kc.F23),
            keyPress(kc.F24),
        ],
        "baseColor":
        Colors.grey,
    },
    {
        "title":
        "1337",
        "keys": [
            keyPress(kc.SHIFT, kc.F),
            keyPress(kc.A),
            keyPress(kc.Q),
            keyPress(kc.TAB),
            keyPress(kc.S),
            keyPress(kc.W),
            keyPress(kc.RETURN),
            keyPress(kc.D),
            keyPress(kc.E),
            keyPress(kc.SPACEBAR),
            keyPress(kc.F),
            keyPress(kc.R),
        ],
        "pixels": [
            Colors.blue,  # SHIFT, F
            Colors.white,  # A
            Colors.lightBlack,  # Q
            
            Colors.yellow,  # TAB
            Colors.white,  # S
            Colors.white,  # W
            
            Colors.orange,  # SPACEBAR
            Colors.white,  # D
            Colors.lightBlack,  # E
            
            Colors.orange,  # SPACEBAR
            Colors.red,  # F
            Colors.green,  # R
        ],
    },
    {
        "keys": [],
        "pixels": [],
    },
]

for key_data in mappings:

    if not "keys" in key_data:
        key_data["keys"] = []
    if len(key_data["keys"]) < 12:
        for _ in range(12 - len(key_data["keys"])):
            key_data["keys"].append('')

    if not "pixels" in key_data:
        key_data["pixels"] = []
    if len(key_data["pixels"]) < 12:
        ki = len(key_data["pixels"])
        for _ in range(12 - len(key_data["pixels"])):
            key_data["pixels"].append(None)
            ki += 1

    for ki in range(12):
        if key_data["pixels"][ki] == None:
            if key_data["keys"][ki] == '':
                key_data["pixels"][ki] = Colors.black
            else:
                if "baseColor" in key_data:
                    key_data["pixels"][ki] = mixColors(
                        colorwheel(int(ki / 12 * 360)), key_data["baseColor"])
                else:
                    key_data["pixels"][ki] = mixColors(
                        colorwheel(int(ki / 12 * 360)), Colors.black)


def evalKeyPressObj(key, hold=False):
    try:
        if isinstance(key, FnKeyMap):
            key.keyDown()
        elif callable(key):
            key()
        elif isinstance(key, list):
            for k in key:
                evalKeyPressObj(k, hold=True)
            macropad.keyboard.release_all()
        # elif key in fKeyMap:
        #     fKeyMap[key]()
        elif isinstance(key, str):
            if key != '':
                macropad.keyboard_layout.write(key)
        elif isinstance(key, int):
            macropad.keyboard.press(key)
            if not hold:
                macropad.keyboard.release_all()
        elif isinstance(key, bytes):
            evalKeyPressObj(int.from_bytes(key))
    except Exception as e:
        print(str(e))


def evalKeyRelease(key, hold=False):
    try:
        if isinstance(key, FnKeyMap):
            key.keyUp()
    except Exception as e:
        print(str(e))


def updateDisplay(index):
    keyData = mappings[index]
    pageTitle = f"Page {index}"
    if 'title' in keyData:
        pageTitle = keyData["title"]
    print(f"{pageTitle}")
    print(f"{''}")
    print(f"{''}")
    print(f"{''}")

    if 'pixels' in keyData:
        ki = 0
        for rgbColor in keyData['pixels']:
            try:
                macropad.pixels[ki] = rgbColor
            except:
                macropad.pixels[ki] = 0
            ki += 1
    else:
        ki = 0
        for kd in keys:
            macropad.pixels[ki] = 0
            ki += 1

    macropad.pixels.brightness = 0.25


mapping_index = 0
last_position = 0
page_changed = True

key_pressed_stack = []

while True:
    time.sleep(0.01)
    macropad.update()

    if macropad.encoder_pressed:
        macropad.keyboard.release_all()
        mapping_index = 0
        page_changed = True

    mapping_index += -macropad.encoder_direction
    if mapping_index < 0:
        mapping_index = len(mappings) - 1
    if len(mappings) <= mapping_index:
        mapping_index = 0

    if page_changed or macropad.encoder_direction != 0:
        page_changed = False
        updateDisplay(mapping_index)

    kmap = mappings[mapping_index]
    keys = kmap['keys']

    while macropad.keys.events:
        key_event = macropad.keys.events.get()

        if key_event.pressed:
            # Append pressed key to the end of the stack
            key_pressed_stack.append(key_event.key_number)
            # print(key_event.key_number, "v")
            evalKeyPressObj(keys[key_event.key_number])
        else:
            # Remove released key from the stack
            key_pressed_stack.remove(key_event.key_number)
            # print(key_event.key_number,"^")
            evalKeyRelease(keys[key_event.key_number])