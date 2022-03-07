from FoxDot.preset import *

change_bpm(110, True)
mi >> mixer()
ss >> sends()
sa >> sca()
sb >> scb()
sc >> scc()


Scale.default = Scale.majorPentatonic
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
b1.dur= Pvar([swing100*4,4],16)
