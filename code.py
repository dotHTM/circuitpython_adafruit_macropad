
from debugHelper import thisDebugPrinter, debugAnounce
# thisDebugPrinter.enabled = True

import time

from MacroPad import thisMacropad as macropad
from settings import mappings, Settings

from settings.helpers import FnKeyMap

from settings.Colors import colorwheel, mixColors, Colors


macropad.update()

x_position = 0 
y_position = 0 



import board
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label


@debugAnounce
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

@debugAnounce
def evalKeyRelease(key, hold=False):
    try:
        if isinstance(key, FnKeyMap):
            key.keyUp()
    except Exception as e:
        print(str(e))

@debugAnounce
def updateDisplay(index, title, labels):
    keyData = mappings[index]
    pageTitle = f"Page {index}"
    if 'title' in keyData:
        pageTitle = keyData["title"]
    
    title.text = f"{pageTitle:^22}"
    
    for i in range(12):
        l = f"KEY{i}"
        if 'desc' in keyData and i < len(keyData['desc']):
            l = keyData['desc'][i]
        labels[i].text = f"{l:^7}"
    
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

import displayio
import terminalio
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_display_text import bitmap_label as label


main_group = displayio.Group()
macropad.display.show(main_group)
title = label.Label(
    y=4,
    font=terminalio.FONT,
    color=0x0,
    text=f"{'Hello!':^22}",
    background_color=0xFFFFFF,
)
layout = GridLayout(x=0, y=10, width=128, height=54, grid_size=(3, 4), cell_padding=1)
labels = []
for _ in range(12):
    labels.append(label.Label(terminalio.FONT, text=""))

for index in range(12):
    x = index % 3
    y = index // 3
    layout.add_content(labels[index], grid_position=(x, y), cell_size=(1, 1))

main_group.append(title)
main_group.append(layout)

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
        updateDisplay(mapping_index, title, labels)

    kmap = mappings[mapping_index]
    keys = kmap['keys']

    while macropad.keys.events:
        key_event = macropad.keys.events.get()

        if key_event.pressed:
            # Append pressed key to the end of the stack
            key_pressed_stack.append(key_event.key_number)
            evalKeyPressObj(keys[key_event.key_number])
            labels[key_event.key_number].color = 0x0
            labels[key_event.key_number].background_color = 0xFFFFFF
        else:
            # Remove released key from the stack
            key_pressed_stack.remove(key_event.key_number)
            evalKeyRelease(keys[key_event.key_number])
            # labels[key_event.key_number].text = ""
            labels[key_event.key_number].color = 0xFFFFFF
            labels[key_event.key_number].background_color = 0x0