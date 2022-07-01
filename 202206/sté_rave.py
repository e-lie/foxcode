from FoxDot.preset import *

sc >> supercollider()
# sv >> sverb(verb_w=1, verb_size=.85)

change_bpm(100)

Scale.default = Scale.majorPentatonic

f1 >> fordrip(0, dur=PRand(1,4), oct=PWalk(7,1,3)[:17]).fadein(24)

m1 >> marimba("ab (ca[cc]d)[ff]", oct=3, dur=cascara, sverb=sinvar([0,.5], 32)).humz()

m2 >> blip([5,2,3, Rest(2)], dur=.25, pan=[-1, 0, 1]).humz()

M = var([(0,2),(2,3)],[8,4,2,2])

m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4)).fadein()

m2.fadein()
