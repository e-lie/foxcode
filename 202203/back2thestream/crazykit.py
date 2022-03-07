from FoxDot.preset import *

change_bpm(90, True)
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

k1 >> kicker("<(aaaA) ><b( B)>", dur=.5, ssc=.7, amp=1.22).sfadeout(32)

k1.amplify = var([1,0])

d4 >> crazykit("tTTtT", dur=cascara)
d2 >> crazykit("wwW", dur=clave23)
e2.phaser_dw = sinvar([0,.6], 17)
e2.hamp_dw = sinvar([0,.3], 9)


m1 >> marimba([0,2,1,0,-2,-5,0,4], dur=cubalet, amp=.7, scale=Scale.minor, oct=5, root=var([0,2,-5], 32)) + (-5,2,7)
m1.humz()
m1.ampfadein(4)

d5 >> crazykit("ssS ", dur=.25, amplify=var([1,0],16)).humz()

m1.amplify=var([.8,0],[48,16])

Clock.bpm=
