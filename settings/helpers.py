
import storage


from MacroPad import thisMacropad as macropad


# def consumer_control_key(key_int):
#     return key_int


def cc(key):

    def inner():
        macropad.consumer_control.send(key)

    return inner


def noop(*args, **kwargs):
    pass



class FnKeyMap():
    keyDown = noop
    keyUp = noop
    desc = None

    def __init__(self, onDown= noop , onUp= noop ) -> None:
        self.keyDown = onDown
        self.keyUp = onUp

    def onKeyDown(self, fn):
        if callable(fn):
            self.keyDown = fn

    def onKeyUp(self, fn):
        if callable(fn):
            self.keyUp = fn
    def __repr__(self) -> str:
        return "<FnKeyMap>"

class keyPress(FnKeyMap):
    
    def __init__(self, *keycodeList):
        super(keyPress, self).__init__()
        def onDown():
            for k in keycodeList:
                macropad.keyboard.press(k)
        def onUp():
            for k in reversed(keycodeList):
                macropad.keyboard.release(k)        
        self.onKeyDown(onDown)
        self.onKeyUp(onUp)

    def __repr__(self) -> str:
        return "<KeyPressObj>"




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

class ResetBoot(FnKeyMap):
    enabled = False
    def __init__(self):
        super(ResetBoot, self).__init__()
        def resetFn():
            if self.enabled:
                storage.remount("/", readonly=False)
                with open("boot.py", "w") as f:
                    f.write('')
                print("boot.py cleared.")
            else:
                print("To Reset,\nPress Again.")
        self.onKeyDown(resetFn)



