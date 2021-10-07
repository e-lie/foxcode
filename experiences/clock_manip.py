

from time import sleep


for it in range(10):
    cc >> pads(I, dur=4, sus=3)
    sleep(4*60/Clock.bpm - 0.1)
    cc >> pads(IV, dur=4, sus=3)
    sleep(4*60/Clock.bpm - 0.1)
    cc >> pads(V, dur=4, sus=3)
    sleep(4*60/Clock.bpm - 0.1)


for b in range(60, 121):
    Clock.bpm = b
    sleep(60/b)
