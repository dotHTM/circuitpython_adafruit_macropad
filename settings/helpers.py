
import storage
from MacroPad import thisMacropad as macropad


# def consumer_control_key(key_int):
#     return key_int


def cc(key):
    def inner():
        if macropad.hostConnected():
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
        if macropad.hostConnected():    
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

class ToneKeeper():
    toneStack = []

class TonePlayer(FnKeyMap):
    def __init__(self, freq) -> None:
        super(TonePlayer, self).__init__()
        def start():
                ## append to the end of the stack
                ToneKeeper.toneStack.append(freq)
                ## stop whatever was playing before
                macropad.stop_tone()
                ## start playing our freq
                macropad.start_tone(freq)
                print(ToneKeeper.toneStack)
        def stop():
                ## if we're the bottom freq, stop playing
                if 0 < len(ToneKeeper.toneStack) and ToneKeeper.toneStack[-1] == freq:
                    macropad.stop_tone()
                ## drop our freq
                while freq in ToneKeeper.toneStack:
                    ToneKeeper.toneStack.remove(freq)
                ## if still frequencies on the stack, play the last one
                if 0 < len(ToneKeeper.toneStack):
                    macropad.start_tone(ToneKeeper.toneStack[-1])
                print(ToneKeeper.toneStack)
                
            
            # ToneKeeper.toneStack.append(freq)
        
        self.onKeyDown(start)
        self.onKeyUp(stop)
        
