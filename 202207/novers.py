from FoxDot.preset.reaper import *
from FoxDot.preset.common import *

change_bpm(110, True, .81)

Scale.default = Scale.majorPentatonic
Root.default = 0

f1 >> fordrip(-20, dur=8).fadein(16)
f1.span(srot(32))
f1 >> fordrip(-10, dur=[8,2])

m_all.amplify = PWhite(.3,1.2)[:8].stutter(8)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=4, amp=sinvar([.1,.9],32), dur=.125).fadein()
m1.span(srot(24))
m1.shuffle()

m2 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=6, amp=sinvar([.1,.9],17), dur=.125, ).humz()
m2.span(srot(16))

m2.dur=brazlet/3

m2.solo(0)

m_all.every(32, "shuffle")

m2.solo(0)
m2.oct = [3,5,7]

tt >> play("< -><x >").mpan(range(6))
tt.dur = cascara
tt.rate = 1

Scale.default = Scale.minor
Scale.default = Scale.egyptian
Scale.default = Scale.majorPentatonic

Scale.default = Pvar([Scale.majorPentatonic, Scale.egyptian, Scale.minor, Scale.chromatic], 32)

m3 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=[4,5,6,7,8], amp=linvar([.5,.9],7), dur=cascara).humz()
# Scale.default = Scale.chromatic
m3.span(srot(32))

m1.solo()
m1.solo(0)

m1.dur=clave23
m2.dur=1

Root.default = var([0,2,-2], [2,4,16,3])

Scale.default = Scale.majorPentatonic

b4 >> blip([5,2,3,2], dur=.25, pan=[-1, 0, 1], amp=1.5).humz()
b4.sus=expvar([.1,1], 16)
b4.mpan(mrot(64))

d1 >> play(" (---[ *])", amp=2)
d1.rate = sinvar([.7,1.8], 23)
d1.mpan(range(6))

f2 >> fordrip2((-20,0,10,40), dur=PRand(1,4), oct=PWalk(7,1,3)[:17])
f2.span(srot(12))

Root.default = var([0,5,-2], 32)

m2.dur=0.125
m1.dur=0.1
m2.dur=1
m1.dur=clave23

m1.solo()
m1.solo(0)

m1 >> marimba("aba([c]a[cccc]d)[ff]", oct=[3,4,3,5], amplify=pa32).humz()

M = var([(0,2),(2,3)],[8,4,2,2])

m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4))
m3.amplify = pa32_3

m2.stop()

# d1 >> play("i", dur=clave23, sample=[2,3], pan=[-1,(-1,1),1], room=4)

m3.every(8, "reverse")

Scale.default = Pvar([Scale.majorPentatonic, Scale.minorPentatonic], 32)

m1.every(16, "reverse")

b4 + P(0, 2, -2)

b4.solo()

b4.mpan(mrot(128))

b4.only()

d_all.stop()

k1 >> play(" -")
k1 >> play("V-").fadein()
k1 >> play("<V(i  i i [ii] i[ii])>< ->")
k2 >> play("x", dur=cascara)
k_all.mpan(mrot(32))

k_all.solo(0)

b4 + P*(0,3,2)

m3.fadeout()
m2.fadeout()
b4.fadeout()

################################################################

k_all.only()

bpm_to(120, 16)

change_bpm(120, True, .81)

Scale.default=Scale.minor
Root.default = 0

b1 >> blip(P[0,2,-3,4].stutter(8), dur=.25, sus=sinvar([.25,1],16), oct=(4,6))
b1.mpan(mrot(32))

f2 >> whibot2(PWalk(7,1,3)[:17], dur=PRand(1,4), oct=6)
f2.faderand()

b2 >> tb303([0,2,4,-5,2], dur=var([.25, 1/3], [24, 8]), sus=sinvar([.25,2],16), oct=(5))
b2.mpan(mrot(7))

Root.default = var([0,2,4,0],[16,8,8,16,8])

d4 >> play(".*[**].", rate=var([1,2]))
d4.mpan(mrot(16))

b1.dur=cascara
b1.dur=.25

k1 >> play("V", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32)

d4.dur=clave23

k1.mpan(mrot(12))

k1.only()

d1 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2)

b3 >> bbass([0,2,4,-5,2], dur=cascara, oct=5) + (0,2)

b3 + (2,4,-5)

d1.amplify=po16

d3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=pa16_3).mpan(mrot(4))

b2.degrade()

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=16, shape=0.5, pan=[-1,-1,1], slide=-1)

k2 >> play("X-", dur=.5, sample=P[0,1,2].stutter(5), amplify=pa32)

e3.amplify=po16_2

f_all.fadeout()

e_all.degrade(0)
d_all.degrade(0)

e_all.fadeout(0)
b_all.fadeout(0)
d_all.fadeout(0)


################################################################

d4 >> play("X-", dur=.5)

b1 >> blip([0,1,-2,4], dur=brafflet, oct=6, shape=.5, sus=linvar([.1, 2],16))

d1 >> play("V-", dur=brafflet, amp=PWhite(.7,1)[:17]*linvar([.8,1.2], 16))
d_all.mpan(mrot(16))

b2 >> pluck([0,1,-2,4], dur=.25, oct=7)

bb >> darkpass([0,2,1,-1], oct=4, dur=8, amplify=pa64)
bb.span(srot(64))

d_all.mpan(mrot(16))

Root.default=0

b_all.sus=sinvar([.1,2],8)

d3 >> play("<v-><I >", dur=clave23)

b2.dur= Pvar([.25, brafflet], [24,8])

d_all.sample = var([0,1,2], 16)

e8 >> play("/", dur=16)
e8.mpan(mrot(32))

d_all.rate = PWhite(.7,2)[:17]

d_all.slide = PWhite(-2,2)[:32]

d_all.mpan(range(6))

b1.mpan(mrot(8))
b2.mpan(mrot(24))

d1.amplify = pa32
d2.amplify = pa32_2
d3.amplify = pa16

k1 >> play("^", amp=3, rate=2.5, dur=cubalet, amplify=po16)
k2 >> play("^", amp=3, rate=4, dur=1/3, amplify=po16_2)

k_all.mpan(mrot(5))

b_all.fadeout()
bb.fadeout()
k_all.fadeout()

################################################################

bpm_to(162)
change_bpm(162, True, .81)
change_bpm(162)

Clock.bpm=162

Root.default = 0

d_all.stop()

d7 >> play("<V.O..Vo.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=.8)

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)

d4 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=pa16_3, pan=var([-1,0,1],2))

d2.every(14, "stutter", 4, dur=3)

d_all.only()
sc >> supercollider()

d_all.mpan(mrot(16))

d_all.degrade()
d_all.rate=1
d_all.crush=8

b2 >> bbass(P[4,2,0].stutter(2), oct=5, dur=[1,1,2], amplify=pa32_2).fadein()
b2.crush = 0

b2 + (2,4)

b2.oct=P[5,6,7].stutter(3)

b_all.root=var([0,-3,0,2],16)
b_all.crush = 0
# b_all.crush = var([0,32,8,64],8)

b3 >> darkpass([0,2,1,-1], oct=4, dur=4, amplify=pa64).fadein()

d8 >> play("/", dur=16, pan=[-1, 0, -1])

d2.every(8, "stutter", 8, dur=6)

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)

d_all.fadeout()

e_all.stop()

b_all.only()

Root.default = 0

d8 >> play("/", dur=8, pan=[-1, 0, -1])

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)

l1 >> loop("200173-breakbeat5.wav", 0, rate=1.35, dur=4)

b_all.fadeout()

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=[1.35, 1.35, -1.35, -2.7], dur=[4,2,2, 1, 1, 1, 1])

d1 >> play("^^^ ", dur=clave23, sample=1)

l1.dur=clave23
l1.dur=4

l2 >> loop("200173-breakbeat5.wav", [0,0,4,2], rate=1.35, dur=[4,4,3,1], pan=[-1,1], amplitude=pa16)

l3 >> loop("200173-breakbeat5.wav", [2,2,0], rate=1.35, dur=1, amplitude=pa16_2)

l3.mpan(mrot(17))
l2.mpan(mrot(7))
l1.mpan(mrot(28))

l3.dur=cascara

l_all.crush=sinvar([0,32], [24,8])

l2.stop()

l1.fadeout()

chords = var([0,5,2,3],[8,4,2,2])

e2 >> blip(chords, dur=.25, amp=.7, sus=sinvar([.25,1],16), oct=(5,6), pan=P[-1,0,1].stutter(2))


l_all.fadeout()

e2.mpan(range(6))

l_all.fadeout()

Root.default = 0

v1 >> vibra(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4, amplify=pa32_3)

v1 + var([(0,2),(2,4)],[28,4,16,16])

d2 >> play("<V.O..Vo.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=.8).fadein()

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3).fadein()

bb >> hpluck(chords, dur=PSum(3,2), sus=1, oct=5, amp=.7, amplify=pa32)

v1 + P*(0,2)

v_all.span(srot(32))

v2 >> marimba2([0,2,4,7,8,2], dur=1/2, sus=1/2, amplify=pa16_2, pan=var([-1, 1], 48), oct=[5,6,7]) + [0,0,[0,0,1]]
v3 >> pluck([0,2,4,7,8,2], dur=1/2, sus=1/2, amplify=pa16_2, pan=var([-1, 1], 48), oct=[3,4,6]) + [0,0,[0,0,1]]

Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.minorPentatonic], [32, 64, 32])

v2 + P(0,2)

v_all.only()

d1 >> play("<xVx ><X >", dur=cascara, amplitude=pa16_2, amp=PWhite(.8,1.2)[:17])
d1.mpan(mrot(17))

d2.amplitude = pa32

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)
e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

v1 + P*(0,2,0,-3)

v1 + P*(0,2,0,4,0,-3)

e1.degrade()
e1.fadeout(64)

d2.degrade()

d1.degrade()

v1.sfadeout(32)

v1 + P*(0,2,0,4,0,-3)

b2.degrade()

v1.only()
v1.degrade()

v1.oct=[2,3,4,5,7]

bpm_to(260, 32)

v1.fadeout(16)
