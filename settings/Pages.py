

# from adafruit_hid.keycode import Keycode as kc
# from .helpers import keyPress, SpecialKeys, TonePlayer
# from .Colors import Colors, colorwheel
# from MacroPad import Notes

# mediaPage = {
#     "title":
#     "Media",
#     "desc": [
#         "Mute", "Vol -", "Vol +", "Esc", "^", "SndSrc", "<", "v", ">", "<<",
#         "|>", ">>"
#     ],
#     "keys": [
#         SpecialKeys.MUTE, SpecialKeys.VOLUME_DECREMENT,
#         SpecialKeys.VOLUME_INCREMENT,
#         keyPress(kc.ESCAPE),
#         keyPress(kc.UP_ARROW),
#         keyPress(kc.CONTROL, kc.SHIFT, kc.OPTION, kc.COMMAND, kc.H),
#         keyPress(kc.LEFT_ARROW),
#         keyPress(kc.DOWN_ARROW),
#         keyPress(kc.RIGHT_ARROW), SpecialKeys.SCAN_PREVIOUS_TRACK,
#         SpecialKeys.PLAY_PAUSE, SpecialKeys.SCAN_NEXT_TRACK
#     ],
#     "pixels":
#     [(255, 0, 0), (255, 255, 0), (0, 255, 0), Colors.orange, Colors.lightBlack,
#      Colors.yellow, Colors.lightBlack, Colors.lightBlack, Colors.lightBlack,
#      colorwheel(0, 0.75, 0.5),
#      colorwheel(120, 0.75, 0.5),
#      colorwheel(240, 0.75, 0.5)]
# }

# phonePad = {
#     "title":
#     "Phone",
#     "desc": [
#         "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[#]",
#         "[0]", "[*]"
#     ],
#     "keys": [
#         keyPress(kc.KEYPAD_ONE),
#         keyPress(kc.KEYPAD_TWO),
#         keyPress(kc.KEYPAD_THREE),
#         keyPress(kc.KEYPAD_FOUR),
#         keyPress(kc.KEYPAD_FIVE),
#         keyPress(kc.KEYPAD_SIX),
#         keyPress(kc.KEYPAD_SEVEN),
#         keyPress(kc.KEYPAD_EIGHT),
#         keyPress(kc.KEYPAD_NINE),
#         keyPress(kc.SHIFT, kc.THREE),
#         keyPress(kc.KEYPAD_ZERO),
#         keyPress(kc.SHIFT, kc.EIGHT)
#     ],
#     "pixels": [
#         Colors.grey, Colors.grey, Colors.grey, Colors.grey, Colors.grey,
#         Colors.grey, Colors.grey, Colors.grey, Colors.grey, Colors.orange,
#         Colors.grey, Colors.orange
#     ],
#     "baseColor":
#     Colors.green
# }

# numberPad = {
#     "title":
#     "Numbers",
#     "desc": ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", ".", "Enter"],
#     "keys": [
#         keyPress(kc.KEYPAD_SEVEN),
#         keyPress(kc.KEYPAD_EIGHT),
#         keyPress(kc.KEYPAD_NINE),
#         keyPress(kc.KEYPAD_FOUR),
#         keyPress(kc.KEYPAD_FIVE),
#         keyPress(kc.KEYPAD_SIX),
#         keyPress(kc.KEYPAD_ONE),
#         keyPress(kc.KEYPAD_TWO),
#         keyPress(kc.KEYPAD_THREE),
#         keyPress(kc.KEYPAD_ZERO),
#         keyPress(kc.KEYPAD_PERIOD),
#         keyPress(kc.KEYPAD_ENTER)
#     ],
#     "pixels": [
#         Colors.white, Colors.white, Colors.white, Colors.white, Colors.white,
#         Colors.white, Colors.white, Colors.white, Colors.white, Colors.white,
#         Colors.orange, Colors.red
#     ]
# }
# fkeysPage = {
#     "title":
#     "F-Keys",
#     "desc": [
#         "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11",
#         "F12"
#     ],
#     "keys": [
#         keyPress(kc.F1),
#         keyPress(kc.F2),
#         keyPress(kc.F3),
#         keyPress(kc.F4),
#         keyPress(kc.F5),
#         keyPress(kc.F6),
#         keyPress(kc.F7),
#         keyPress(kc.F8),
#         keyPress(kc.F9),
#         keyPress(kc.F10),
#         keyPress(kc.F11),
#         keyPress(kc.F12)
#     ],
#     "baseColor":
#     Colors.black
# }

# fkeysHiPage = {
#     "title":
#     "F-Upper",
#     "desc": [
#         "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22",
#         "F23", "F24"
#     ],
#     "keys": [
#         keyPress(kc.F13),
#         keyPress(kc.F14),
#         keyPress(kc.F15),
#         keyPress(kc.F16),
#         keyPress(kc.F17),
#         keyPress(kc.F18),
#         keyPress(kc.F19),
#         keyPress(kc.F20),
#         keyPress(kc.F21),
#         keyPress(kc.F22),
#         keyPress(kc.F23),
#         keyPress(kc.F24)
#     ],
#     "baseColor":
#     Colors.grey,
# }

# leetPage = {
#     "title":
#     "1337",
#     "desc": [
#         "F", "^ a", "q", "Esc", "< s", "> w", "Return", "v d", "e", "Space",
#         "f", "r"
#     ],
#     "keys": [
#         keyPress(kc.SHIFT, kc.F),
#         keyPress(kc.A),
#         keyPress(kc.Q),
#         keyPress(kc.ESCAPE),
#         keyPress(kc.S),
#         keyPress(kc.W),
#         keyPress(kc.RETURN),
#         keyPress(kc.D),
#         keyPress(kc.E),
#         keyPress(kc.SPACEBAR),
#         keyPress(kc.F),
#         keyPress(kc.R)
#     ],
#     "pixels": [
#         Colors.blue,  # SHIFT, F
#         Colors.white,  # A
#         Colors.lightBlack,  # Q
#         Colors.yellow,  # TAB
#         Colors.white,  # S
#         Colors.white,  # W
#         Colors.orange,  # SPACEBAR
#         Colors.white,  # D
#         Colors.lightBlack,  # E
#         Colors.orange,  # SPACEBAR
#         Colors.red,  # F
#         Colors.green  # R
#     ],
# }

# musicChromaticPage = {
#     "title":
#     "Chromatic",
#     'desc': ["G#", "E", "C", "A", "F", "C#", "A#", "F#", "D", "B", "G", "D#"],
#     "keys": [
#         # TonePlayer(440),
#         TonePlayer(Notes.Gs),
#         TonePlayer(Notes.E),
#         TonePlayer(Notes.C),
#         TonePlayer(Notes.A),
#         TonePlayer(Notes.F),
#         TonePlayer(Notes.Cs),
#         TonePlayer(Notes.As),
#         TonePlayer(Notes.Fs),
#         TonePlayer(Notes.D),
#         TonePlayer(Notes.B),
#         TonePlayer(Notes.G),
#         TonePlayer(Notes.Ds)
#     ],
#     "pixels": [
#         Colors.lightBlack, Colors.white, Colors.white, Colors.white,
#         Colors.white, Colors.lightBlack, Colors.lightBlack, Colors.lightBlack,
#         Colors.white, Colors.white, Colors.white, Colors.lightBlack
#     ]
# }

# musicCPage = {
#     "title":
#     "Key of C",
#     'desc':
#     ["D2", "G1", "C1", "E2", "A1", "D1", "F2", "B1", "E1", "G2", "C2", "F1"],
#     "keys": [
#         # TonePlayer(440),
#         TonePlayer(Notes.D * 2),
#         TonePlayer(Notes.G),
#         TonePlayer(Notes.C),
#         TonePlayer(Notes.E * 2),
#         TonePlayer(Notes.A),
#         TonePlayer(Notes.D),
#         TonePlayer(Notes.F * 2),
#         TonePlayer(Notes.B),
#         TonePlayer(Notes.E),
#         TonePlayer(Notes.G * 2),
#         TonePlayer(Notes.C * 2),
#         TonePlayer(Notes.F)
#     ],
#     "pixels": [
#         colorwheel(1 * 360 / 7),
#         colorwheel(4 * 360 / 7),
#         colorwheel(0 * 360 / 7),
#         colorwheel(2 * 360 / 7),
#         colorwheel(5 * 360 / 7),
#         colorwheel(1 * 360 / 7),
#         colorwheel(3 * 360 / 7),
#         colorwheel(6 * 360 / 7),
#         colorwheel(2 * 360 / 7),
#         colorwheel(4 * 360 / 7),
#         colorwheel(0 * 360 / 7),
#         colorwheel(3 * 360 / 7)
#     ]
# }
