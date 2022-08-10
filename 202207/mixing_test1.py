from FoxDot.preset import *

Clock.bpm = 143

l1 >> loop("Voiski - Bloodthirsty Romantic Shark - loop1", [0], dur=4, lpf=5000, hpf=00, amp=2)

l1 >> loop("Hadone - How To Fake Success - Original mix - 143 - Crop #2", [.2], dur=16, lpf=2000, hpf=00, amp=linvar([1,1.6]))

l1 >> loop("Hadone - How To Fake Success - Original mix - 143 - Crop #2", [8.2], dur=16, lpf=2000, hpf=00, amp=linvar([1,1.6]))

l1 >> loop("Hadone - How To Fake Success - Original mix - 143 - Crop #2", [64.2], dur=32, lpf=2000, hpf=00, amp=linvar([1,1.6]))

l1 >> loop("Hadone - How To Fake Success - Original mix - Crop #2", [64.2], dur=32, lpf=2000, hpf=00, amp=linvar([1,1.6]))

d1 >> play("X(-=-[ -- ])", dur=P[.5]<<[0,-.05,0,-.1], sample=PStutter([2,3],3), room=3, amp=[.8,1.2], crush=4, rate=.7)

b1 >> blip([0,2,-2,-5], dur=.25, oct=[4,5,6])
b2 >> blip([0,2,-2,-5], dur=.25, oct=[4,5,6])

Scale.default = Scale.egyptian

b1.oct = [2,5,8,4,6,3]

b1.sus= linvar([.1, 2], 8)

b2.crush = 16
b2.dur=[.4,.3,.3]

Root.default = var([0,4,-2],8)
