# import json

# class Settings():
#     def __init__(self) -> None:
#         self._storage = {}
#         with open("settings.json", "r") as f:
#             self._storage = json.loads(f.read())
    
#     def get(self, key):
#         if key in self._storage:
#             return self._storage[key]
#         return None
    
#     def set(self, key, value):
#         self._storage[key] = value
    
#     def write(self):
#         print('## FIXME write settings')
#         pass


# settings = Settings()