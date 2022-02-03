# import storage

# import json

# settings = {}
# try:
#     with open("settings.json", "r") as f:
#         settings = json.loads(f.read())
# except Exception as e:
#     print(e)

# if 'disk' in settings:
#     if settings['disk']:
#         storage.enable_usb_drive()
#     else:
#         storage.disable_usb_drive()
