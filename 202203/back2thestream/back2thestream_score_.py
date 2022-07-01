from FoxDot.preset import *

change_bpm(110, True)
mi >> mixer()
ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()


e6 >> crazykit("uU", dur=8)
e2 >> crazykit("fF", dur=P[7,1,8,3,5]/2, amp=[.6,.7,.9,1.23])

d3 >> crazykit("hH(HHHi)", dur=cubalet, oct=3, amp=[.9,1.22]*PWhite(.7,1)[:17]).humz().every(8, "stutter", 2)

e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 9)

d1 >> crazykit("aA bB", oct=3, scale=Scale.major, root=0, amp=PWhite(.1,1.2)[:17], dur=cascara, resob_dw=.7)

d3.solo()
d3.phaser_dw = .4

k1 >> kicker("<(aaaA) ><b( B)>", dur=.5, ssc=.7, amp=1.22)
k1.sfadeout(32)

k1.amplify = var([1,0])

d4 >> crazykit("tTTtT", dur=cascara)
d2 >> crazykit("wwW", dur=clave23)
e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 9)

d2.sfadeout(16)

d2.only()

Clock.bpm = bpmto(100, 16)

change_bpm(100, True)


Scale.default = Scale.minorPentatonic
.default =


m1 >> marimba('<ab(dadD) ABD >', dur=cascara, oct=3)
m3 >> marimba('<cC >', dur=cascara, oct=3)
m4 >> marimba('<h h h h>', dur=cascara, oct=3)
m2 >> marimba('(aG) ', dur=clave23, oct=[6,7,5]).every(8, "stutter", 3)

m1.i_overtone=var([0,.1,.5],16)
m1.phaser_dw = .6


m1.amplify = var([1,0],[24,8])
m3.amplify = var([0,1],[8,24])
m2.amplify = var([1,0],[2,6])
m4.amplify = var([0,1],[7,3,8])


Clock.bpm = sinvar([100, 120], 32) * sinvar([.9,1.1],27)

m1.i_tone = sinvar([0,.9],32)

Root.default = var([0,1,3], [3,7,9,12])


k1 >> kicker("(f)", ssc=1, amp=1.2)
k2 >> kicker("aba ", ssc=1, amp=1.2, dur=cascara)

d1 >> crazykit("<bB(bBb )><Ss >", dur=cubalet).humz()
d1.every(12, "stutter", 3)

m1.fadeout(32)

Root.default = 0
Scale.default = Scale.major

change_bpm(110, True)


d2 >> crazykit("ffff f fff f ff", dur = cascara, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16))
d3 >> crazykit("F f FFF F ", dur = clave23, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16))
d3 >> crazykit("q q", dur = cascara*4, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16), vol=1)
d4 >> kit808("w ww www wwww", dur=clave23, amp=1.2)

te >> crazykit("FFF(f )", dur = Pvi(triplet, binlet, 16))
t2 >> crazykit("Hhhh").humz()
t2.phaser_dw = .6

b1 >> owstr([0,2,-5,2,4,0], dur=4, root=var([0,4,2,-5],8))
b1.amplify=var([.8,0], [24,8])

# play with params

b1.dur= Pvar([swing100*4,4],16)

d1 >> kit808("H ", dur=cascara, amp=1.2)
d2 >> kit808("w", dur=clave23, amp=.9).humz()

k1 >> kicker([0,9], oct=3, ssc=.8, dur=1).every(16, "stutter", 3)

b1 >> crubass([0,0,2,-5,0,-2], oct=3, dur=[2,2,1,3])
b1.fadein(16)

# play with params

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
d3 >> crazykit("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

d4 >> play("/", dur=16, output=2)

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.8,1.2)[:17], ssc=.8)

b1.fadeout(16)

b1 >> tb303([0,0,2,-5,0,-2], oct=3)
b1.dur = swing100*2

b1.sus = swing100*2 - 0.03

b1.dur = swing100/2
b1.hamp_dw = .5

Clock.bpm = bpmto(120, 32)

k1.sfadeout(32)
