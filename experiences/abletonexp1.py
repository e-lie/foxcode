from time import sleep
import live
import random

set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)

Clock.bpm = 100
Clock.meter = (6,8)


print(set)

piano1 = Instruc(1, 6, Clock)


piano2 = Instruc(1, 4, Clock)

percu = Instruc(2, 2, Clock)

kit808 = Instruc(3, 2, Clock)

advoca = Instruc(4, 3, Clock)

advoca2 = Instruc(4, 3, Clock)

wonkbass = Instruc(5, 3, Clock)

piano1.display_set()

aa >> MidiOut([7], channel=1, dur=1, sus=0.95, amp=0.3)

piano1.update(pitch=[I, IV, I, V, IV], dur=1, sus=0.2, amp=0.8, oct=6)
piano1.update(pitch=[P+(I), IV, P+(II), I, I, P+(VI)])
piano1.update(dur=1, sus=1)
piano1.update(amp=PWhite(0.5,0.9)[:30])
piano1.update(dur=[8/10,6/10,6/10])
piano1.set_param(1, linvar([0,127],16), update_freq=0.5)
piano1.set_param(3, linvar([0,127],8), update_freq=0.1)

piano1.later(16,dur=[4/10,3/10,3/10])

piano1.later(16,dur=[2/7,3/7,3/7])

piano1.later(16,dur=[1/2,1/4,1/4])

piano1.later(16, amp=0.1)

piano1.later(16, dur=1/2)

piano1.stop(16)

piano1.amp=PWhite(0.5,0.8)[:20]

piano1.set_param(8, 100)


piano1.stop()

piano1.dur=PWhite(1)[:10]

for i in range(10):
    piano1.amp=i*0.02
    sleep(0.3)

advoca.update([0, 4, 7], amp=PWhite(0.1,0.9)[:20], dur=[4/10, 3/10, 3/10], oct=4)

advoca.update(amp=PWhite(0.1, 0.6)[:10])

advoca.update(pitch=[0,4,0,7], dur=[5/10,6/10,3/10,6/10], sus=P[5/10,6/10,3/10,6/10]-0.01)

advoca2.update([0, 4, 7], amp=PWhite(0.1,0.9)[:20], dur=[1/2], oct=3)
advoca2.stop()

advoca.update([0, 2, 12], amp=PWhite(0.3,0.6)[:20], dur=1/2, oct=5)

advoca.set_param(1, linvar([0.0,1.0],8), update_freq=0.1)

advoca.amp = 0.7

percu.update([10], dur=[1/2,1/4,1/4], amp=0.5)

percu.update(P(10,9), dur=[8/10,6/10,6/10], amp=PWhite(0.7,0.9)[:10])

percu.update([10], dur=[3/7,2/7,2/7], amp=PWhite(0.4,0.9)[:20])

percu.update([12], dur=[1/3, 1/3, 1/3], amp=PWhite(0.7,0.9)[:10])

percu.stop()

percu.update([12], dur=[1/2,1/4,1/4], amp=PWhite(0.8,1)[:10])

kit808.update(P[7,8,7,8], dur=[3/4, 1/4, 1/2, 1/2])
kit808.amp=P[1, 0.6, 1, 0.6]

kit808.stop()



piano2.stop()
