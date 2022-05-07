from FoxDot.preset import *

change_bpm(110, True)
mi >> mixer()
# ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()



aa >> play("X-", dur=[4/10,3/10,3/10]*2, sample=var([0,1,2],1), output=[2,4,6])
cc >> play("w w ", dur=1/2, sample=var([0,1,2],1), output=[2,4,6])

e6 >> crazykit("uU", dur=8, vol=.2).span(linvar([0,5.9], 8))

e2 >> crazykit("fF", dur=P[7,1,8,3,5]/2, amp=[.6,.7,.9,1.23], scale=Scale.major)

d3 >> crazykit("hh(hhhi)", dur=cubalet, oct=3, amp=[.9,1.22]*PWhite(.7,1)[:17], vol=0).humz().every(8, "stutter", 2)
d3.span(linvar([0,5.9], 8))

e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 9)

d1 >> crazykit("aA bB", oct=3, scale=Scale.major, root=0, amp=PWhite(.1,1.2)[:17], dur=cascara, resob_dw=.7)

d3.solo()
d3.phaser_dw = .4

k1 >> kicker("<(aaaA) ><b( B)>", dur=.5, ssc=.7, amp=1.22, vol=.8).sfadeout(32)

k1.amplify = var([1,0])

d4 >> crazykit("tTTtT", dur=cascara)
d2 >> crazykit("wwW", dur=clave23)
e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 9)

k1.fadeout(16)

d2.only()

Clock.bpm = bpmto(100, 16)

change_bpm(100, True)


Scale.default = Scale.majorPentatonic
.default =


m1 >> marimba('<ab(dadD) ABD >', dur=cascara, oct=3, amp=.4)
m3 >> marimba('<cC >', dur=cascara, oct=5, amp=.4)
m4 >> marimba('<h h h h>', dur=cascara, oct=3)
m2 >> marimba('(aG) ', dur=clave23, oct=[5,6,5], amp=1.2).every(8, "stutter", 3)
m2.span(linvar([0, 5.9], [16, 0]))


m1.i_overtone=var([0,.1,.5],16)
m1.phaser_mod_rate = sinvar([0,.4],16)


m1.amplify = var([1,0],[4,8])
m3.amplify = var([0,1],[8,24])
m2.amplify = var([1,0],[2,6])
m4.amplify = var([0,1],[7,3,8])


Clock.bpm = sinvar([100, 120], 32) * sinvar([.9,1.1],27)

m1.i_tone = sinvar([0,.9],32)

Root.default = var([0,1,3], [3,7,9,12])


k1 >> kicker("(f)", ssc=1, amp=1.2).stop()
k2 >> kicker("aba ", ssc=1, amp=1.2, dur=cascara).stop()

d1 >> crazykit("<bB(bBb )><Ss >", dur=cubalet).humz()
d1.every(12, "stutter", 3)

m1.fadeout(32)

Root.default = 0
Scale.default = Scale.minor

change_bpm(110, True)

d1.stop()
d2 >> crazykit("ffff f fff f ff", dur = cascara, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16))
d3 >> crazykit("h f hhh h ", dur = clave23, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16))
d3 >> crazykit("q q", dur = cascara*4, scale=Scale.major, amp=PWhite(.5,1.2)[:17], reverb_dw=sinvar([.2,.6],32), reverb_decay=sinvar([0,.8],16), vol=1)

d4 >> crazykit("w ww www wwww", dur=clave23, amp=1.2)
d4.span(linvar([0,5.9],[12,0]))

te >> crazykit("aaa(f )", dur = Pvi(triplet, binlet, 16)).stop()
t2 >> crazykit("Hhhh").humz()
t2.phaser_dw = .6

b1 >> mavimba([0,2,-5,2,4,0], dur=4, root=var([0,4,2,-5],8))
b1.amplify=var([.8,0], [24,8])

# play with params

b1.dur= Pvar([swing100*4,4],16)

d1 >> vibra(0, dur=cascara, amp=1.2, root=PTri(0,8,2).stutter(4), oct)

d2 >> crazykit("w", dur=clave23, amp=.9).humz()

k1 >> kicker([0,9], oct=3, ssc=.8, dur=(1).every(16, "stutter", 3)

b1 >> crubass([0,0,2,-5,0,-2], oct=3, dur=[2,2,1,3]).span(linvar([0,5.9], [8,0]))

b1.setp(crubass_1)
b1.fadein(16)

# play with params

d2.amplify = d1.amplify = var([1,0],[48,16])

m1.degree = Pvz([
    ("h ", 16),
    ("h(hhh) ", 16),
    ("hh", 16),
])

b1.dur = swing100*2.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

b1.sus = swing100*2 - 0.03

mi.phaser_dw=.6

d1.reverb_dw = sinvar([0,.5],16)

d2.fadein(16)

d3 >> crazykit("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

d1.stop()

d4 >> play("/", dur=16, amp=2).mpan(range(6))

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.8,1.2)[:17], ssc=.8)
k1 >> play("<VxX ><X >", dur=cascara, amp=PWhite(.8,1.2)[:17], ssc=.8).mpan(range(6))

b1.fadeout(16)

b1 >> tb303([0,0,2,-5,0,-2], oct=3)
b1.dur = swing100*2
b1.sus = swing100*2 - 0.03

b1.dur = swing100/2
b1.hamp_dw = .5

Clock.bpm = bpmto(120, 32)

k1.sfadeout(32)
