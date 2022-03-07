from FoxDot.preset import *

Clock.clear()

change_bpm(150, True, 0.26)
bb >> mixer()
ss >> sends()

t1 >> play("-=--   -=-=", sample=PRand(0,4)).stop()
d2 >> kit808("<--h-----=><(     w) w>", sreverb=1)

ss.sreverb_decay = var([.1,.9],4) * linvar([0,1],4)

t1.amp=PWhite(0,.9)[:17]
d2.amp=PWhite(0,.8, seed=2)[:17]

d3 >> kitcuba("bb(btbt)b(  t)(  t)", amp=[.7,1], dur=gnawa*2, eq_gain=.6)

d4 >> kicker(1, dur=var([1,2],16), amp=var([1,0], [12,4,24,8]))

b3 >> ubass([3,4,5]*2 + [1,1], dur=[2,2,3,1], sus=[2,2,3,1], oct=4)

b3.ubass_cutoff = linvar([0,1], 16)

b3.stop()

b3.setp(rndp(danceorgp, 2))

b3.root = var([0, 0, 0, 0, -2, 0, 2, 0], 8)
b3.hamp_dw = .6
bb.hamp_dw=.7
b3.vol = .7
b3.reverb_dw =.4


p1 >> kit808("x-", dur=Pvi([.25,.25,.5],[1/3])).fadein(16)
p1.stop()

b1 >> crubass([0,2,4], amp=1.3).stop()
