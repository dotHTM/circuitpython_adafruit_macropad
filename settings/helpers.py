# import storage
# from MacroPad import thisMacropad as macropad
# from .Settings import settings

# # def consumer_control_key(key_int):
# #     return key_int


# def cc(key):

#     def inner():
#         if macropad.hostConnected():
#             macropad.consumer_control.send(key)

#     return inner


# def noop(*args, **kwargs):
#     pass


# class FnKeyMap():

#     def __init__(self, onDown=noop, onUp=noop, desc='<key>', labelObj=None ) -> None:
#         if onDown != None:
#             self.keyDown = onDown
#         if onUp != None:
#             self.keyUp = onUp
        
#         self.labelObj = labelObj

#     def onKeyDown(self, fn):
#         if callable(fn):
#             self.keyDown = fn

#     def onKeyUp(self, fn):
#         if callable(fn):
#             self.keyUp = fn
    
#     def updateDisplay(self):
#         if self.labelObj != None:
#             self.labelObj.text = str(self)
            
    
#     def __repr__(self) -> str:
#         return self.desc

# class keyPress(FnKeyMap):

#     def __init__(self, *keycodeList, desc='key'):
#         super(keyPress, self).__init__(desc=desc)
#         if macropad.hostConnected():
#             def onDown():
#                 for k in keycodeList:
#                     macropad.keyboard.press(k)
#             def onUp():
#                 for k in reversed(keycodeList):
#                     macropad.keyboard.release(k)
#             self.onKeyDown(onDown)
#             self.onKeyUp(onUp)


# class SpecialKeys():
#     BRIGHTNESS_DECREMENT = cc(
#         macropad.ConsumerControlCode.BRIGHTNESS_DECREMENT)
#     BRIGHTNESS_INCREMENT = cc(
#         macropad.ConsumerControlCode.BRIGHTNESS_INCREMENT)

#     RECORD = cc(macropad.ConsumerControlCode.RECORD)

#     REWIND = cc(macropad.ConsumerControlCode.REWIND)
#     PLAY_PAUSE = cc(macropad.ConsumerControlCode.PLAY_PAUSE)
#     FAST_FORWARD = cc(macropad.ConsumerControlCode.FAST_FORWARD)

#     STOP = cc(macropad.ConsumerControlCode.STOP)
#     SCAN_NEXT_TRACK = cc(macropad.ConsumerControlCode.SCAN_NEXT_TRACK)
#     SCAN_PREVIOUS_TRACK = cc(macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK)

#     MUTE = cc(macropad.ConsumerControlCode.MUTE)
#     VOLUME_DECREMENT = cc(macropad.ConsumerControlCode.VOLUME_DECREMENT)
#     VOLUME_INCREMENT = cc(macropad.ConsumerControlCode.VOLUME_INCREMENT)

#     EJECT = cc(macropad.ConsumerControlCode.EJECT)


# class ResetBoot(FnKeyMap):
#     enabled = False

#     def __init__(self):
#         super(ResetBoot, self).__init__()

#         def resetFn():
#             if self.enabled:
#                 storage.remount("/", readonly=False)
#                 with open("boot.py", "w") as f:
#                     f.write('')
#                 print("boot.py cleared.")
#             else:
#                 print("To Reset,\nPress Again.")

#         self.onKeyDown(resetFn)



# class ToggleBoot(FnKeyMap):
#     localEnable = True

#     def __init__(self) -> None:
#         def onDown():
#             self.localEnable = not self.localEnable
#         super().__init__(onDown, labelObj=labelObj)
        
#     def __repr__(self) -> str:
#         return "Toggle"+str( 1 if  self.localEnable else 0 )







# class ToneKeeper():
#     toneStack = []

# class TonePlayer(FnKeyMap):

#     def __init__(self, freq) -> None:
#         super(TonePlayer, self).__init__()

#         def start():
#             ## append to the end of the stack
#             ToneKeeper.toneStack.append(freq)
#             ## stop whatever was playing before
#             macropad.stop_tone()
#             ## start playing our freq
#             macropad.start_tone(freq)
#             print(ToneKeeper.toneStack)

#         def stop():
#             ## if we're the bottom freq, stop playing
#             if 0 < len(
#                     ToneKeeper.toneStack) and ToneKeeper.toneStack[-1] == freq:
#                 macropad.stop_tone()
#             ## drop our freq
#             while freq in ToneKeeper.toneStack:
#                 ToneKeeper.toneStack.remove(freq)
#             ## if still frequencies on the stack, play the last one
#             if 0 < len(ToneKeeper.toneStack):
#                 macropad.start_tone(ToneKeeper.toneStack[-1])
#             print(ToneKeeper.toneStack)

#         # ToneKeeper.toneStack.append(freq)

#         self.onKeyDown(start)
#         self.onKeyUp(stop)
