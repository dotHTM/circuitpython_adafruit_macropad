# from .helpers import ResetBoot, ToggleBoot

# from .Colors import Colors, colorwheel, mixColors
# from .Pages import musicCPage,  musicChromaticPage,  mediaPage,  numberPad,  phonePad,  fkeysPage,  fkeysHiPage,  leetPage

# from MacroPad import thisMacropad as macropad

# settingsPage = {
#     "title": "Settings",
#     "keys":[ToggleBoot()],
#     "pixels": [Colors.yellow, 0, 0, 0, 0, 0, 0, 0, 0, 0, Colors.red, 0],
# }

# # def hostConnected():
# #     try:
# #         macropad.keyboard._keyboard_device
# #         return "Hosted"
# #     except Exception as e:
# #         return "Isolated"

# import sys


# def asList(iterableObj, mapping=lambda e: e):
#     result = []
#     for i in iterableObj:
#         result.append(mapping(i))
#     return result


# infoPage = {
#     "title":
#     "Info",
#     "desc": [
#         'python',
#         '',
#         sys.version,
#         str(sys.implementation.name),
#         '',
#         ".".join(asList(sys.implementation.version, mapping=lambda e: str(e))),
#         '',
#         '',
#         '',
#         '',
#         '',
#         "Hosted" if macropad.hostConnected() else "Self",
#     ]
# }

# mappings = [
#     infoPage,
#     musicCPage,
#     musicChromaticPage,
# ]
# if macropad.hostConnected():
#     mappings = [
#         settingsPage,
#         mediaPage,
#         numberPad,
#         phonePad,
#         fkeysPage,
#         fkeysHiPage,
#         leetPage,
#         musicCPage,
#         musicChromaticPage,
#         infoPage,
#     ]

# defaultKeyData = {"keys": "", "desc": '', "pixels": Colors.black}

# for thisMapping in mappings:
    
#     for k in defaultKeyData:
#         v = defaultKeyData[k]
#         if not k in thisMapping or not isinstance(thisMapping[k], list):
#             thisMapping[k] = []
#         for i in range(12):
#             if len(thisMapping[k]) <= i:
#                 thisMapping[k].append(v)

#     for ki in range(12):
#         if thisMapping["keys"][ki] == '' or thisMapping["keys"][ki] == None:
#             thisMapping["pixels"][ki] = Colors.black
#         else:
#             if thisMapping["pixels"][ki] == None:
#                 thisMapping["pixels"][ki] = colorwheel(int(ki / 12 * 360))
#             if "baseColor" in thisMapping:
#                 thisMapping["pixels"][ki] = mixColors(thisMapping["pixels"][ki],
#                                                    thisMapping["baseColor"])
