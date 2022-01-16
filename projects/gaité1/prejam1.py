change_bpm(120)
bb >> mixer()
Clock.midi_nudge = 0.78 # 60
Clock.midi_nudge = 0.38 # 100
Clock.midi_nudge = 0.28 # 120
Clock.midi_nudge = 0.21 # 140
Clock.midi_nudge = 0.16 # 160

s1 >> strings(P[0,2,4], dur=[4,3,5], vol=.8)

d3 >> play("x", amp=1, dur=1)
d1 >> kit808(" -", amp=1)

t1 >> crubass([0,2,4], dur=gnawa, sus=gnawa-0.03, **rndp(crubassp, 12), oct=3, pan=sinvar([-1,1],4))
d2 >> kicker([(1,6), 11], amp=1, dur=1, **delay(subdiv=1/3, feedback=.9)).every(8, "stutter", 3)

d4 >> play("<funky><  (ew)l>", rate=4*PRand([1,1.5,1.25]), dur=var([1/4,1/2], 16), pan=PStep(6,P*(-1,1)))

s1 >> owstr(P[0,2,4], dur=[4,3,5], root=var([0,2,4,5,0],16))
s1 >> owstr(P[0,2,4], dur=[4,3,5], root=var([0,2,4,5,0],16))

bb >> mixer(delay_vol=0)

t1 >> crubass_2([0,2,4], dur=gnawa, sus=gnawa-0.03, oct=2)

t1 >> crubass([0,2,4], dur=gnawa, sus=gnawa-0.03, **rndp(crubassp, 12), oct=3, pan=sinvar([-1,1],4))
