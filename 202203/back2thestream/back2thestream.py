from FoxDot.preset import *

change_bpm(110, True)
mi >> mixer()
ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()

rhythms = {
"half" : P[1/2],
"swing100" : P[4/10,6/10],
"swing" : P[3/10,7/10],
"triplet" : P[1/3],
"binlet" : P[1/2,1/4,1/4],
"cubalet" : P[4/10,3/10,3/10],
"binlet2" : P[1/4,1/2,1/4],
"gnawa" : P[3/10,4/10,3/10],
"quarter" : P[1/4],
"brazlet" : P[3/10,1/5,1/5,3/10],
"brazlet100" : P[1/3,1/6,1/6,1/3],
"quintuplet" : P[1/5],
"brafflet" : P[3/12,2/12,2/12,2/12,3/12,2/12],
"clave" : P[3/15,3/15,4/15,2/15,3/15],
"clave23" : P[3/16,3/16,4/16,2/16,4/16]*4,
"cascara" : P[2/16,2/16,1/16,2/16,1/16,2/16,1/16,2/16,2/16,1/16]*4,
}

e1 >> crazykit("uU", dur=8)
e2 >> crazykit("fF", dur=P[7,1,8,3,5]/2, amp=[.6,.9,1.1,.7])

d3 >> crazykit("hH(HHHi)", dur=cubalet, amp=[.9,.7,1]*PWhite(.7,1)[:17]).every(8,"stutter",2)

e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 17)

d1 >> crazykit("aA bB", dur=cascara, amp=[.9,.7,1]*PWhite(.7,1)[:17]).every(8,"stutter",2)

k1 >> kicker("<(aaaA) ><b( B)>", dur=.5, ssc=.7).every(16, "stutter", 3)

d4 >> crazykit("tTTtT", dur=cascara)
d2 >> crazykit("ww(W )", dur=clave23)

d2.sfadeout(32)
d2.only()

change_bpm(100)

Scale.default=Scale.majorPentatonic

m1 >> marimba('ab(dadD) AB', dur=cascara, oct=3)
m2 >> marimba('cC ', dur=cascara, oct=3)
m3 >> marimba('h h h h ', dur=cascara, oct=3)
m4 >> marimba('(aG) ', dur=clave23, oct=[5,6]).every(8,"stutter", 3)

m1.i_overtone=var([0,.1,.5], 16)
m1.phaser_dw = .6

Clock.bpm = sinvar([100,120], 64)

m1.i_tone = sinvar([0,.9], 32)

k1 >> kicker("f", ssc=.8)
k2 >> kicker("aba ", ssc=.8, dur=cascara)

Clock.bpm=bpmto(110)

Scale.default = Scale.major

m1.fadeout(32)

k1.only()

d1 >> crazykit("fff f ff f  ff", dur=cascara, amp=PWhite(.5, 1.2)[:17], reverb_dw=sinvar([.2, .6], 32), reverb_decay=sinvar([0, .8], 32))
d2 >> crazykit("F Ff FFF", dur=clave23, amp=PWhite(.5, 1.2)[:17], reverb_dw=sinvar([.2, .6], 32), reverb_decay=sinvar([0, .8], 32))
d3 >> crazykit("q q", dur=cascara*4, amp=PWhite(.5, 1.2)[:17], reverb_dw=sinvar([.2, .6], 32), reverb_decay=sinvar([0, .8], 32))
d4 >> kit808("w ww wwwwwww", dur=clave23)

b1 >> owstr([0,2,-5,4,2,0], dur=4, root=var([0,4,2,-5], 8))
b1.amplify = var([.8, 0], [24,8])

b1.dur=Pvar([swing100*4,4],16)

d4.sfadeout(32)
d4.only()

d1 >> kit808("H ", dur=cascara, amp=1.2)

k1 >> kicker([0,9], ssc=.8)

b1 >> crubass([0,0,2,-5,0,-2], oct=3, dur=[2,2,1,3])

d1.degree = Pvz([
    ("H ", 16),
    ("H(hhH) ", 16),
    ("Hh", 16)
])

mi.phaser_dw=.5

d3 >> kit808("sss ", dur=var([.25,.125], 16), amp=PWhite(.6,1)[:17])

d4 >> play("/", dur=16 , output=2)

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.6,1.1)[:27], ssc=.8, amplify=1)

k1.sfadeout(32)


# Thx all for watching :{:{:{:{key: value for key, value in variable}: value for key, value in variable}: value for key, value in variable}: value for key, value in variable}
# Good night
