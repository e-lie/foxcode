from FoxDot.preset import *

change_bpm(110, True)
mi >> mixer()
ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()

d1 >> kit808("H ", dur=cascara, amp=1.2)
d2 >> kit808("w", dur=clave23, amp=.9).humz()

k1 >> kicker([0,9], oct=3, ssc=.8, dur=1).every(16, "stutter", 3)

b1 >> crubass([0,0,2,-5,0,-2], oct=3, dur=[2,2,1,3])
b1.setp(crubass_1)
b1.fadein(16)

d2.amplify = d1.amplify = var([1,0],[48,16])

d1.degree = Pvz([
    ("H ", 16),
    ("H(hhH) ", 16),
    ("Hh", 16),
])

b1.dur = swing100*2
b1.sus = swing100*2 - 0.03

mi.phaser_dw=.6

d1.reverb_dw = sinvar([0,.5],16)

d2.fadein(16)

d3 >> kit808("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

d4 >> play("/", dur=16, output=2)

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.8,1.2)[:17], ssc=.8)

b1.fadeout(16)

b1 >> tb303([0,0,2,-5,0,-2], oct=3, dur=stutter([2,2,1,3],2))

b1.dur = swing100/2
b1.hamp_dw = .5

Clock.bpm = bpmto(120, 32)
