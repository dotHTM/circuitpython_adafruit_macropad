

from MacroPad import MacroPad

from colorsys import hsv_to_rgb

macropad = MacroPad()


def cc(key):

    def inner():
        macropad.consumer_control.send(key)

    return inner


fKeyMap = {
    "\\RECORD":
    cc(macropad.ConsumerControlCode.RECORD),
    "\\FAST_FORWARD":
    cc(macropad.ConsumerControlCode.FAST_FORWARD),
    "\\REWIND":
    cc(macropad.ConsumerControlCode.REWIND),
    "\\SCAN_NEXT_TRACK":
    cc(macropad.ConsumerControlCode.SCAN_NEXT_TRACK),
    "\\SCAN_PREVIOUS_TRACK":
    cc(macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK),
    "\\STOP":
    cc(macropad.ConsumerControlCode.STOP),
    "\\EJECT":
    cc(macropad.ConsumerControlCode.EJECT),
    "\\PLAY_PAUSE":
    cc(macropad.ConsumerControlCode.PLAY_PAUSE),
    "\\MUTE":
    cc(macropad.ConsumerControlCode.MUTE),
    "\\VOLUME_DECREMENT":
    cc(macropad.ConsumerControlCode.VOLUME_DECREMENT),
    "\\VOLUME_INCREMENT":
    cc(macropad.ConsumerControlCode.VOLUME_INCREMENT),
    "\\BRIGHTNESS_DECREMENT":
    cc(macropad.ConsumerControlCode.BRIGHTNESS_DECREMENT),
    "\\BRIGHTNESS_INCREMENT":
    cc(macropad.ConsumerControlCode.BRIGHTNESS_INCREMENT),
}


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
            "\\MUTE",
            "\\VOLUME_DECREMENT",
            "\\VOLUME_INCREMENT",
            macropad.Keycode.ESCAPE,
            "",
            [
                macropad.Keycode.CONTROL,
                macropad.Keycode.SHIFT,
                macropad.Keycode.OPTION,
                macropad.Keycode.COMMAND,
                macropad.Keycode.H,
            ],
            "",
            "",
            "",
            '\\REWIND',
            '\\PLAY_PAUSE',
            '\\FAST_FORWARD',
        ],
        "pixels": [
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            Colors.orange,
            None,
            None,
            None,
            None,
            None,
            colorwheel(0, 0.75, 0.5),
            colorwheel(120, 0.75, 0.5),
            colorwheel(240, 0.75, 0.5),
        ]
    },
    {
        "title":
        "Numbers",
        "keys": [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '.',
            '0',
            macropad.Keycode.RETURN,
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
            macropad.Keycode.F1,
            macropad.Keycode.F2,
            macropad.Keycode.F3,
            macropad.Keycode.F4,
            macropad.Keycode.F5,
            macropad.Keycode.F6,
            macropad.Keycode.F7,
            macropad.Keycode.F8,
            macropad.Keycode.F9,
            macropad.Keycode.F10,
            macropad.Keycode.F11,
            macropad.Keycode.F12,
        ],
        "baseColor":
        Colors.darkGrey,
    },
    {
        "title":
        "F-Upper",
        "keys": [
            macropad.Keycode.F13,
            macropad.Keycode.F14,
            macropad.Keycode.F15,
            macropad.Keycode.F16,
            macropad.Keycode.F17,
            macropad.Keycode.F18,
            macropad.Keycode.F19,
            macropad.Keycode.F20,
            macropad.Keycode.F21,
            macropad.Keycode.F22,
            macropad.Keycode.F23,
            macropad.Keycode.F24,
        ],
        "baseColor":
        Colors.grey,
    },
    {
        "title":
        "1337",
        "keys": [
            macropad.Keycode.TAB,
            "f",
            "r",
            "q",
            "w",
            "e",
            "a",
            "s",
            "d",
            " ",
            [
                macropad.Keycode.SHIFT,
                "f",
            ],
            " ",
        ],
        "pixels": [
            Colors.orange,
            Colors.yellow,
            Colors.green,
            Colors.grey,
            Colors.white,
            Colors.grey,
            Colors.white,
            Colors.white,
            Colors.white,
            Colors.orange,
            Colors.orange,
            Colors.orange,
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


def evalKey(key, hold=False):
    try:
        if isinstance(key, list):
            for k in key:
                evalKey(k, hold=True)
            macropad.keyboard.release_all()
        elif key in fKeyMap:
            fKeyMap[key]()
        elif isinstance(key, str):
            if key != '':
                macropad.keyboard_layout.write(key)
        elif isinstance(key, int):
            macropad.keyboard.press(key)
            if not hold:
                macropad.keyboard.release_all()
        elif isinstance(key, bytes):
            evalKey(int.from_bytes(key))
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

while True:
    macropad.update()

    if macropad.encoder_pressed:
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

    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            kmap = mappings[mapping_index]
            keys = kmap['keys']
            key_index = 0
            for k in keys:
                if key_event.key_number == key_index:
                    evalKey(k)
                key_index += 1
