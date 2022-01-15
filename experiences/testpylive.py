import live
import random
from time import sleep

#------------------------------------------------------------------------
# Scan the set's contents and set its tempo to 110bpm.
#------------------------------------------------------------------------
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)

for track in set.tracks:
    print(track.name)
    # for device in track.devices:
        # print(device.name)
#
# set.tracks[1].devices[0].parameters[1].value = 80
#
# print(set.tracks[1].devices[0].parameters)
#
#
# import random
# track = set.tracks[4]
# print(track.name)
# device = track.devices[0]
# parameter = random.choice(device.parameters)
# parameter.value = random.uniform(parameter.minimum, parameter.maximum)
