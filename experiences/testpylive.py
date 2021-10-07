import live
import random
from time import sleep

#------------------------------------------------------------------------
# Scan the set's contents and set its tempo to 110bpm.
#------------------------------------------------------------------------
set = live.Set()


set.scan(scan_clip_names = True, scan_devices = True)


for track in set.tracks:
    for device in track.devices:
        print(device.name)
