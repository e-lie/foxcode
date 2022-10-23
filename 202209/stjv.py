from FoxDot.preset import *


Scale.default = Pvar([Scale.major, Scale.minor, Scale.egyptian], 16)
Scale.default = Scale.minor

Root.default = var([0,5,0,7],8)
Root.default = var([0,0,5,5,0,0,7,4],4)

Clock.bpm = 120
#linvar([60,200],32)

d=PSum(3,2)
mel=P[0,2,-2,5]

b1 >> blip(
    mel,
    dur=d,
    oct=[3,4,3],
    sus=linvar([.1,3],32),
    crush=49)

b2 >> blip(
    mel + 2,
    dur=d+0.3,
    oct=[5,4,5],
    sus=linvar([.1,3],32),
    amplify=1,
    crush=100)

b3 >> blip(
    mel + 4,
    dur=d+0.3,
    oct=[5,4,5],
    amplify=1,
    sus=linvar([.1,3],32),
    crush=4)



b4 >> pluck([0,2,-2,4], dur=clave23, oct=[3,4,5], sus=linvar([.1,3],32)).pause(4,16)

b2 >> blip([0,2,-2,4], dur=[.25], oct=6).pause(4,16,6)

d1 >> play("i", dur=cascara, crush=12, amp=1, sample=var([0,2,1,3])).pause(8,32,16)

d2 >> play("(*.x.*V.*[xx]*.xX**.xVx[xx]x)", dur=cascara, sample=0, pan=[-1,1], rate=linvar([.7,3],16), crush=var([2,4,clave23,64])).pause(4,32,24)
d1 >> play("(*.x.*V.*[xx]*.xX**.xVx[xx]x)", dur=cascara, sample=0, pan=[-1,1], rate=linvar([.7,3],16), crush=var([2,4,clave23,64])).pause(4,32,24)

d3 >> play("(VVV[VV])( =)", sample=3).ampfadeout()

d2.solo()
b1.solo()


d4 >> epiano([0,4,2,5],dur=.25).stop()
d1 >> bbass([0,2,-2], oct=3, dur=[1,.5])
d2 >> play("-[---]--[----]--)", sample=3, rate=var([1,2,3]), crush=16)
d3 >> play("(I[I][I])(---=)", sample=0)
d3 >> play("(I[I][I])(---=)", sample=0, dur=cascara)
d5 >> play("(v[vv]).*.", sample=0, rate=1, crush=0, dur=.5, amp=1.5)
d5 >> play("(V[VV]).*.", sample=0, rate=1, crush=0, dur=Pvar([.5,clave23], 16), amp=1.5)
p1 >> blip([3,1,-2], dur=1/2)
p1 >> blip([3,1,-2], dur=var([.5, 1/3],8))
p2 >> blip([0,5,2,3], oct=6, dur=[1.5,.5,1,.5,.5], slide=-1)
p2 >> blip([0,5,2,3], oct=6, dur=.25, slide=-1)
