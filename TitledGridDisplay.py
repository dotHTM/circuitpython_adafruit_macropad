
from MacroPad import MacroPad
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
import displayio
import terminalio

from adafruit_display_text import bitmap_label


class TitledGridDisplay():
    
    _rawTitleText = ""
    _rawLabelText = []
    
    def __init__(self, macropad: MacroPad, cols=3, rows=4, titleWidth = 22, labelWidth = 7) -> None:
        
        self._macropad = macropad
        self._display = self._macropad.display
        self._main_group = displayio.Group()
        self._display.show(self._main_group)
        
        self.titleWidth = titleWidth
        self.labelWidth = labelWidth
        
        self._title = bitmap_label.Label(
            y=4,
            font=terminalio.FONT,
            text="",
            color=0x0,
            background_color=0xFFFFFF,
        )
        
        self._layout = GridLayout(
            x=0,
            y=10,
            width=128,
            height=54,
            grid_size=(cols, rows),
            cell_padding=1,
        )
        self._labels = []
        for i in range(cols * rows):
            self._rawLabelText.append('')
            self._labels.append(bitmap_label.Label(terminalio.FONT, text=''))
            self.setLabel(i, '')
        for x in range(cols):
            for y in range(rows):
                index = y * cols + x
                self._layout.add_content(
                    self._labels[index],
                    grid_position=(x, y),
                    cell_size=(1, 1),
                )

        self._main_group.append(self._title)
        self._main_group.append(self._layout)
    
    def update(self):
        if self._macropad.sleeping:
            self.setTitle('', True)
            for i in range(len(self._labels)):
                self.setLabel(i, '', True)
        
    def setTitle(self, newValue, sleepTalking = False):
        if self._rawTitleText != newValue:
            self._rawTitleText = newValue
            if not self._macropad.sleeping and not sleepTalking:
                self._title.text = f"{newValue:{self.titleWidth}}"
    
    def setLabel(self, index, newValue, sleepTalking = False):
        if self._rawLabelText[index] != newValue:
            self._rawLabelText[index] = newValue
            if not self._macropad.sleeping and not sleepTalking:
                self._labels[index].text = f"{newValue:{self.labelWidth}}"
    