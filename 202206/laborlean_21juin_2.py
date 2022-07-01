from FoxDot.preset import *

sc >> supercollider()

change_bpm(100, True, .81)

Scale.default = Scale.majorPentatonic
Root.default = 0

f1 >> fordrip(-20, dur=8).fadein(32)

m1 >> marimba("ab c", oct=3).humz()

f1 >> fordrip(-20, dur=8)
f2 >> fordrip2((-20,0,10,40), dur=PRand(1,4), oct=PWalk(7,1,3)[:17])

m1 >> marimba("aba(ca[cc]d)[ff]", oct=3, amplify=pa32).humz().span(srot(17), .8)

m2 >> blip([5,2,3,2], dur=.25, pan=[-1, 0, 1], amp=1.5).humz()

Root.default = var([0,5,-2], 32)

M = var([(0,2),(2,3)],[8,4,2,2])

m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4))

m3.amplify = pa32_3

d1 >> play("i", dur=clave23, sample=[2,3], pan=[-1,(-1,1),1], room=4)
d2 >> play("iI", dur=cascara, sample=[0,1], pan=[-1,(-1,1),1], room=4)

m3.every(8, "reverse")

Scale.default = Pvar([Scale.majorPentatonic, Scale.minorPentatonic], 32)

m1.every(16, "reverse")

m2 + P*(0,2)
m2 + P*(0,3,2)
m2 + P*(0,2,8)

k1 >> play("V ")

################################################################

m3.fadeout()
m2.fadeout()


bpm_to(120, 16)
change_bpm(120, True, .81)

Scale.default=Scale.minor
Root.default = 0


bb >> blip(P[0,2,-3,4].stutter(8), dur=.25, sus=sinvar([.25,1],16), oct=(4,6), pan=P[-1,0,1].stutter(2))

f2 >> whibot2(PWalk(7,1,3)[:17], dur=PRand(1,4), oct=6)
f2.faderand()

b1 >> tb303([0,2,4,-5,2], dur=var([.25, 1/3], [24, 8]), sus=sinvar([.25,2],16), oct=(4,6), pan=P[-1,0,1].stutter(2))
b1.fadein()

Root.default = var([0,2,4,0],[16,8,8,16,8])

b1 >> tb303([0,2,4,-5,2], dur=cascara, sus=sinvar([.25,2],16), oct=(4,6), pan=P[-1,0,1].stutter(2))

k1 >> play("V ", sample=var([0,2,3],16))
k1 >> play("V-", sample=var([0,2,3],16))

d3 >> play(".*[**].", rate=var([1,2]))

k2 >> play("X", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, pan=[-1, 0, 1])

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2)

k2 >> play("<Xv Xvv>", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, pan=[-1, 0, 1])

d1.amplify=po16

b2 >> bbass([0,2,4,-5,2], dur=cascara, oct=5) + P(0,2)

b2.degrade()

d3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=pa16_3, pan=var([-1,0,1],2))

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)
e3.amplify=po16_2

################################################################

k1.fadeout()
e3.fadeout()
b2.fadeout()
k2.fadeout()
d3.fadeout()

bpm_to(162)
change_bpm(162)

Root.default = 0

d2 >> play("<V.O..Vo.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=.8).fadein()

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)

b1 >> darkpass([0,2,1,-1], oct=4, dur=4, amplify=pa64).fadein()

d3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=pa16_3, pan=var([-1,0,1],2))

d2.every(14, "stutter", 4, dur=3)

b2 >> bbass(P[4,2,0].stutter(2), oct=5, dur=[1,1,2], amplify=pa32_2).fadein()

b2 + (2,4)

b2.oct=P[5,6,7].stutter(3)

b_all.root=var([0,-3,0,2],16)
b_all.crush = var([0,32,8,64],8)

d8 >> play("/", dur=16, pan=[-1, 0, -1])

d2.every(8, "stutter", 8, dur=6)

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)

################################################################

d_all.fadeout()
e_all.stop()
b_all.only()

Root.default = 0

l1 >> loop("200173-breakbeat5.wav", 0, rate=1.35, dur=4)

d8 >> play("/", dur=8, pan=[-1, 0, -1])

b_all.fadeout()

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=1.35, dur=[4,2,2, 1, 1, 1, 1])

d1 >> play("^", dur=clave23, sample=1)
l1.dur=clave23

l2 >> loop("200173-breakbeat5.wav", [0,0,4,2], rate=1.35, dur=[4,4,3,1], pan=[-1,1], amplitude=pa16)

l3 >> loop("200173-breakbeat5.wav", [2,2,0], rate=1.35, dur=1, pan=[1,0,-1], amplitude=pa16_2)

l3.dur=cascara

e2 >> blip(chords, dur=.25, amp=.7, sus=sinvar([.25,1],16), oct=(7,9), pan=P[-1,0,1].stutter(2))

chords = var([0,5,2,3],[8,4,2,2])

l_all.fadeout()

Root.default = 0

Scale.default = Scale.minor

bb >> tb303(chords, dur=PSum(3,2), oct=4, amp=.7, amplify=pa32)

bb.span(srot(64), 1)

v1 >> vibra(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4, amplify=pa32_3)

v1 + var([(0,2),(2,4)],[28,4,16,16])

d2 >> play("<V.O..Vo.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=.8).fadein()

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)

v1 + P*(0,2)

Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.minorPentatonic], [32, 64, 32])

v2 >> marimba2([0,2,4,7,8,2], dur=1/2, sus=1/2, amplify=pa16_2, pan=var([-1, 1], 48), oct=[5,6,7]) + [0,0,[0,0,1]]

v2 + P(0,2)

d1 >> kicker("<hHh ><f >", dur=cascara, amplitude=pa16_2, amp=PWhite(.8,1.2)[:17])

d2.amplitude = pa32

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

################################################################

v1 + P*(0,2,0,-3)
v1 + P*(0,2,0,-3)
v1 + P*(0,2,0,4,0,-3)

d_all.only()

d1.amplify)

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=1.35, dur=[4,2,2, 1, 1, 1, 1])

l1.rate=2.70

v2 >> marimba2([0,2,4,7,8,2], dur=1/2, sus=1/2, amplify=pa16_2, pan=var([-1, 1], 48), oct=[5,6,7]) + [0,0,[0,0,1]]

bb >> hpluck(chords, dur=PSum(3,2), oct=4, amp=.7, amplify=pa32)

v1 >> vibra(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4, amplify=pa32_3)
v1 + var([(0,2),(2,4)],[28,4,16,16])

e_all.degrade()
e_all.fadeout(64)

d_all.degrade()
l_all.degrade()

Clock.bpm = sinvar([160,140, 180], 32)

d1.degrade()

v1 + P*(0,2,0,4,0,-3)

v1.sfadeout(32)

b2.degrade()

v1.only()
v1.degrade()

v1.oct=[2,3,4,5]

bpm_to(320, 32)

v1.fadeout(32)
