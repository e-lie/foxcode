from FoxDot.preset import *


D = P[.5, .25, 1].stutter(4)

V = linvar([.25,3], 16)


v2 >> blip([0,2,4,7,8,2], dur=D, sus=D*V, amplify=pa16_2, pan=var([-1, 1], 8), oct=[5,6,7]) + [0,0,[0,0,1]]
v3 >> click([0,2,4,7,8,2], dur=cascara, sus=cascara*V, amplify=pa16, pan=var([-1, 1], 17), oct=[5,6,7]) + [0,0,[0,0,1]]
v3.oct=4

v4 >> hpluck([0,2,4,7,8,2], dur=cubalet, sus=cubalet*V, amplify=pa32, pan=var([-1, 1], 5)) + [0,0,[0,0,1]]
v4.oct=var([3,4,5], 16)

v_all.humz()

d1 >> play("<*[***] *[**]><VV(VV.)V(V..)>", dur=clave23, sample=P[0,2,2,1,3].stutter(5), rate=sinvar([.5, 2], 48)).fadein()
d1.every(12, "stutter", 4)

d2 >> play("nn( n)", dur=cubalet, sample=0, amp=2)
d2 >> play("-~( (~[nn]))", dur=cubalet, sample=0, amp=2)

Root.default = var(P[0,-5,3,2,-12,1,2,3,4], PRand(1,16))

Clock.bpm = linvar([100,160],64)

change_bpm(140)

d_all.fadeout()

dd.stop()
