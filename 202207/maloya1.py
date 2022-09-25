from FoxDot.preset import *


Scale.default=Scale.minor

Clock.bpm = 78
l1 >> loop("Maloya Ton Tisane1", [7.3], dur=8, lpf=5000, hpf=00, amp=4, rate=.76)
d1 >> play("X ", amp=4, dur=.5).stop()

Clock.bpm = 104
l1 >> loop("Maloya Ton Tisane1", [7.7], dur=8, lpf=5000, hpf=00, amp=2, rate=1)
l1.crush = 32

d1 >> play("X ", amp=3, dur=.5).stop()

l2 >> loop("Hadone - How To Fake Success - Original mix - 143 - Crop #2", [256.7], dur=8, rate=104/143)

l2 >> loop("Hadone - How To Fake Success - Original mix - 143 - Crop #2", [49.7], dur=8, rate=104/143)


l2.only()

Clock.bpm = 95

Clock.meter =(5,8)

k2 >> play("(XXX[ X])", amp=6, dur=.5, rate=1.2, hpf=5000)
k1 >> play("(XXX[ X]) ", amp=3, dur=.5, rate=1.2, lpf=200, sample=P[0].stutter(4), crush=2, bits=4)

d2 >> play("V  V ", amp=4)

d3 >> play("s", amp=6, dur=P[.4,.3,.3])

d3 >> play("s", amp=6, dur=P[.4,.3,.3]<<PWhite(-0.05,.05)[:67])
d3 >> play("s", amp=6, dur=P[.5,.25,.25]<<[0,.13,.06, 0, .09, .05])


d4 >> play("(V) ", amp=1, dur=clave23<<[0,.1,.05,.05,.1], rate=1.2, hpf=1000)


d2 >> play("x[xx]xx[xx]", amp=P[1.3,.7,1,.9,1.2], dur=clave23<<[0,.1,.05,.05,.1])
d2.crush=var([2,4,8,16,32])
d2.bits=var([2,4,8])
d3 >> play("s", amp=1, dur=P[.5,.25,.25]<<[0,.13,.06, 0, .09, .05])
d3.crush=var([2,4,8,16,32])
d3.bits=var([2,4,8])


p1 >> blip(PWalk()[:36], dur=P[.5,.25,.25]<<[0,.11,.05, 0, .1, .05], amp=1)
p1.oct=[3,4,4,5]


d_all.crush=2
d_all.rate=0

p1 >> pluck([0,0,0,(0,2,4)], dur=P[Rest(2/3),2/3,1,5/3], amp=.6).stop()


p1 >> pluck([0,0,0,0,(0,2,4)], dur=clave23, amp=.4)

print(clave23)

Clock.bpm = 107.5
l1 >> loop("Maloya Ton Tisane2", [0.3], dur=8, lpf=5000, hpf=00, amp=2)
d1 >> play("V ", amp=1)
