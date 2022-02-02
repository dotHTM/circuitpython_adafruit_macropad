
import json

from .keymap import mappings
from .Colors import Colors, colorwheel, mixColors


class Settings():
    def __init__(self) -> None:
        self._storage = {}
        with open("settings.json", "r") as f:
            self._storage = json.loads(f.read())
    
    def get(self, key):
        if key in self._storage:
            return self._storage[key]
        return None
    
    def set(self, key, value):
        self._storage[key] = value
    
    def write(self):
        print('## FIXME write settings')
        pass





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
        if key_data["keys"][ki] == '' or key_data["keys"][ki] == None:    
            key_data["pixels"][ki] = Colors.black
        else:
            if key_data["pixels"][ki] == None:
                key_data["pixels"][ki] = colorwheel(int(ki / 12 * 360))
            if "baseColor" in key_data:
                key_data["pixels"][ki] = mixColors( key_data["pixels"][ki] , key_data["baseColor"])
                
