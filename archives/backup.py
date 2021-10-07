from time import sleep
import live
import random

set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)

Clock.bpm = 100

print(set)

for i, track in enumerate(set.tracks):
    print("\n" + str(i) + " - " + str(track))
    print("===========================")
    for j, device in enumerate(track.devices):
        print(str(j) + " - " + str(device))
        print("------------------------------------")
        for k, parameter in enumerate(device.parameters):
            print(str(k) + " - " + str(parameter))

piano2 = Instruc(1, 4, Clock)
piano1 = Instruc(1, 6, Clock)

percu = Instruc(2, 2, Clock)
percu2 = Instruc(2, 2, Clock)

kit808 = Instruc(3, 2, Clock)
advoca = Instruc(4, 3, Clock)




aa >> MidiOut([7], channel=1, dur=1, sus=0.95, amp=0.3)


piano1.setup([I, IV, I, V, IV], dur=2, sus=1.99, amp=0.8, oct=6)
piano1.amp=PWhite(0.5,0.8)[:20]

piano1.set_param(8, linvar([60,127],16), update_freq=0.1)

piano1.set_volume(127)

c =

set_volume(c)

print(type(c))

piano1.stop()

piano1.dur=PWhite(1)[:10]

for i in range(10):
    piano1.amp=i*0.02
    sleep(0.3)

advoca.setup([0, 4, 7], amp=PWhite(0.3,0.6)[:20], dur=1/2, oct=4)

advoca.setup([0, 2, 12], amp=PWhite(0.3,0.6)[:20], dur=1/2, oct=5)

advoca.amp = 0.7

percu.setup([10], dur=[1/2,1/4,1/4], amp=0.5)

percu.setup(P(10,9), dur=[8/10,6/10,6/10], amp=PWhite(0.7,0.9)[:10])

percu.setup([9], dur=[8/10,6/10,6/10], amp=PWhite(0.7,0.9)[:10])

percu.setup([12], dur=[1/3, 1/3, 1/3], amp=PWhite(0.7,0.9)[:10])

percu.stop()

percu.setup([12], dur=[1/2,1/4,1/4], amp=PWhite(0.8,1)[:10])

# percu.stop()
kit808.setup(P[7,8,7,8], dur=[3/4, 1/4, 1/2, 1/2])
kit808.amp=P[1, 0.6, 1, 0.6]

kit808.stop()


cc >> play("x[ f]xf")

piano2.stop()



# Clock.midi_nudge=0.25
