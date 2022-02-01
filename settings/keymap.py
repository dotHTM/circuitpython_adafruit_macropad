from .helpers import cc, noop, FnKeyMap, keyPress, SpecialKeys, ResetBoot

from adafruit_hid.keycode import Keycode as kc

from .Colors import Colors, colorwheel, mixColors

media = {
    "title":
    "Media",
    "desc":[

    "mute", 
    "V--",
        "V++",
        "esc",
        "^",
        "SndSrc",
        "<",
        "v",
        ">", 
        "<<",
        "|>", 
        ">>"
    ],
    "keys": [
        SpecialKeys.MUTE, SpecialKeys.VOLUME_DECREMENT,
        SpecialKeys.VOLUME_INCREMENT,
        keyPress(kc.ESCAPE),
        keyPress(kc.UP_ARROW),
        keyPress(kc.CONTROL, kc.SHIFT, kc.OPTION, kc.COMMAND, kc.H),
        keyPress(kc.LEFT_ARROW),
        keyPress(kc.DOWN_ARROW),
        keyPress(kc.RIGHT_ARROW), SpecialKeys.SCAN_PREVIOUS_TRACK,
        SpecialKeys.PLAY_PAUSE, SpecialKeys.SCAN_NEXT_TRACK
    ],
    "pixels":
    [(255, 0, 0), (255, 255, 0), (0, 255, 0), Colors.orange, Colors.lightBlack,
     Colors.yellow, Colors.lightBlack, Colors.lightBlack, Colors.lightBlack,
     colorwheel(0, 0.75, 0.5),
     colorwheel(120, 0.75, 0.5),
     colorwheel(240, 0.75, 0.5)]
}

numpad = {
    "title":
    "Numbers",
    
    "desc" : [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    ".", "0", "Enter",
    ],
    
    
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
        keyPress(kc.KEYPAD_ENTER)
    ],
    "pixels": [
        Colors.white, Colors.white, Colors.white, Colors.white, Colors.white,
        Colors.white, Colors.white, Colors.white, Colors.white, Colors.orange,
        Colors.white, Colors.red
    ],
}
fkeys = {
    "title":
    "F-Keys",
    "desc" : [
    "F1", "F2", "F3",
    "F4", "F5", "F6",
    "F7", "F8", "F9",
    "F10", "F11", "F12",
    ],
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
        keyPress(kc.F12)
    ],
    "baseColor":
    Colors.darkGrey,
}

fkeysHi = {
    "title":
    "F-Upper",
    
    "desc" : [
    "F13", "F14", "F15",
    "F16", "F17", "F18",
    "F19", "F20", "F21",
    "F22", "F23", "F24",
    ],
    
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
        keyPress(kc.F24)
    ],
    "baseColor":
    Colors.grey,
}

leet = {
    "title":
    "1337",
    
    "desc" : [
    "F", "^ a", "q",
    "Esc", "< s", "> w",
    "Return", "v d", "e",
    "Space", "f", "r",
    ],
    
    "keys": [
        keyPress(kc.SHIFT, kc.F),
        keyPress(kc.A),
        keyPress(kc.Q),
        keyPress(kc.ESCAPE),
        keyPress(kc.S),
        keyPress(kc.W),
        keyPress(kc.RETURN),
        keyPress(kc.D),
        keyPress(kc.E),
        keyPress(kc.SPACEBAR),
        keyPress(kc.F),
        keyPress(kc.R)
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
        Colors.green  # R
    ],
}

settingsPage = {
    "title":
    "Settings",
    "keys": [
        None, None, None, None, None, None, None, None, None, None,
        ResetBoot(), None
    ],
    "pixels": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Colors.red, 0],
}

mappings = [media, numpad, fkeys, fkeysHi, leet, settingsPage]

