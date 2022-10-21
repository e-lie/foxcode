from FoxDot.preset import *


Root.default = var([0,2,-2], 4)

Root.default = 0
p_all.stop()

b1 >> pluck([0,-2,4], dur=cascara, slide=0, oct=5, sus=linvar([.1, 3], 7)).pause(2,16)

b1 + P(0,2)

b1.stop()

b2 >> bbass(P[0,2,-2].stutter(5), dur=cascara, slide=0, oct=var([3,2,4])).pause(6,16, 10)

b1.stop()

b1.stop()


d1 >> play("(XX[XX]XXX[XX]xx[xV])(-[-*]-[ *])", dur=.5, amp=1, rate=linvar([1,1.7],16), sample=3).pause(0,16,8) #####
d2 >> play("(--)", dur=brafflet, amp=2, crush=0, rate=2).pause(6,16,8) #####

d1 >> play("x(-x-[--][**])", sample=var([0,1,2]), bits=16,d7 >> play("b", dur=[.5,1,1,.5], sdb=4, sample=0, rate=1, amp=linvar([0,1],7)).mpan(mrot(16))
 amp=.3, crush=linvar([0,32],16)).pause(8,32,12)

d1.ampfadeout()

################################################################

d1 >> play("V(-[**]-[--])", crush=0, bits=4, amp=1, sample=PRand(0,4)).mpan(0)

d7 >> play("A", dur=clave23, sdb=4, sample=1, rate=1, chop=4, amp=linvar([0,1],7)).mpan(mrot(16))

################################################################
Scale.default="minorPentatonic"

p1 >> play(".(---[-(m-)])", sample=var(P[:4],32)).every([60,4], "alt", "X")

p1 >> play(".(---[-(m-)])", sample=var(P[:4],32)).every([60,4], "alt", "X")

p2 >> play("(Vvvv)", dur=clave23, sample=var(P[:4],32)).mpan(mrot(16)).stop()
b1 >> bbass(PStep(4,7), dur=PSum(3,2), sus=1, amp=0.4, cut=linvar([.5,1]), oct=5)

m1 >> marimba([0,1,-2], dur=cascara, oct=P[4,5].stutter(2), vol=1.2) + P(0,2)

m2 >> marimba([0,1,-2], dur=.25, oct=3, vol=1.2).stop()

b1 >> blip(0, dur=cascara, oct=var([6,7],16), amp=1, sus=linvar([0,3], 32)) + P(0,4)

Clock.bpm = linvar([100,130],[62,inf],start=now)

p1 >> play("(XX{X#}{[oo][Xo][OO][XxXx]}).", sample=2, amp=.6)
p1 >> play("X.x.X.X.X.X.X.[tt]O", sample=var(PRand(8),64), amp=1.5, dur=.5, formant=PStep(4,8))
p2 >> play("-", sample=3, amp=2, rate=linvar([1,3],9), dur=PDur([5,7],8))
p5 >> play("oo[oo][oo.o]", amp=Ramp()*4)

p_all.stop()
p_all.reset()

p3 >> play("<.**><iii.>", dur=clave23, amp=1, rate=1).pause(4,16)
p4 >> play("x..xx.", dur=.5, amp=1, rate=1).pause(4,16,6)

#b2 >> blip([0,2,4,-2], dur=.25, oct=[7,6], amp=2, sus=2, slide=0) - var([0,2,4,-2])
b1 >> blip([0,2,7,-2,0], dur=PSum(5,3), oct=3, amp=3, sus=2, slidefrom=-1)

p3 >> play(Pvar("a","a","a","a","a","a","a","a"), dur=.25, sample=PRand(6), amp=linvar([.45,1.15]), cut=1, slide=PRand(5))
#p3 >> prophet(var([0,2,-1,4],4)+P(0,2,4), dur=.5, amp=.2)
b1 >> jbass(PStep(4,7), dur=PDur([8,5],8), sus=1, amp=0.4, cut=linvar([.5,1]))
b4 >> bell(PRand(-2,7)[:16], dur=[.5,.25,.25], cut=.5, formant=var(PRand(5)), slide=PRand(0,5), chop=b2.dur*[2,4,0,4], amp=0.8)

g1.stop()
l1 >> pluck([0,2,4,-1],dur=2, amp=2, echo=0, blur=2, chop=l1.dur*[2,4]) + P(0,2,4)

p_all.stop()

Master().hpf = var([0,1000],[64-8,8])
Master().hpf = 0

d4 >> jbass(Pvar([0,[0,6,8,0]],[15,1]), dur=.75, amp=var([1.3,0],2), cut=.5, oct=var([5,6],[12,12,4,4]))

s7 >> sawbass(PRand([0,2,4,6]), oct=7, dur=[.25,.25,.5])
