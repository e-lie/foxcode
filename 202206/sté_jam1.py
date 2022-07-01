from FoxDot.preset import *

sc >> supercollider()
sv >> sverb()

change_bpm(100)


Scale.default = Scale.minorPentatonic
=M = var([(0,2),(2,3)],[8,4,2,2])

m1 >> marimba('<ab(da[dd]D) [AA]BD ><k >', dur=cascara, oct=3, amplify=pa16, verb_w=0)
m1.fadein()
m1.humz()

m2 >> blip([5,2,3, Rest(2)], dur=clave23, oct=[4,5,7], pan=[-1,0,1])
m2.fadein()

m3 >> marimba2(M + [[2,0,0],0,[0,2,2],[0,0,2]], dur=cascara, oct=5, amplify=po32)
m3.humz()


d1 >> play("[i*]", amp=linvar([0,1,0],[2,0,2]), rate=2, crush=8, pan=[-1,1])

d2 >> play("ss[ss][ss]", dur=clave23, sample=5, amplify=po32)

m1.every(16, "reverse")

Scale.default = Pvar([Scale.majorPentatonic, Scale.minorPentatonic], 32)

Root.default = var([0,5,-2], 32)

m1.oct=(2,3)

m2 + P*(0,3,2)

m3.every(8, "reverse")

m2.fadeout()


d2.fadeout()

m3.fadeout()

m2.only()

bpm_to(120, 16)

bb >> blip([0], root=var([0,4,-5,0,2], PRand(0,4)[:16]), dur=.25)

Scale.default=Scale.minor

b1.fadein()
b1 >> tb303([0,2,4,-5,2], dur=cascara, oct=3)
b1.root = var([0,2,4,0],[16,8,8,16,8])

dd >> ducker(0, sus=.5, ducking=.4)
k1 >> play("X(---[--])", sample=(0,1), amp=[1.2,.8])

d1 >> play(".*[.*].", amplify=po16)

k2 >> play("<VxxVX>< (.*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4))

Group(d3, k2, k1).only()

b2 >> bbass([0,2,4,-5,2], dur=cascara, oct=6).degrade() + (0,2)

m1.amplify = pa32

d3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=po16_3, pan=var([-1,0,1],2))
d4 >> play("t{t.}", dur=cascara, sample=P[0,1,2].stutter(4), amplify=pa32_3)

d3.fadeout()
d1.fadeout()
k1.fadeout()

################################################################

b1.fadeout()

d2 >> play("<v.O..vo.>", dur=.5, sample=0, rate=linvar([.8,1.2], 16), amp=.8)

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)

b1 >> darkpass([0,2,1,-1], oct=4, dur=4)

bpm_to(160)
change_bpm(160)

b2 >> bbass(P[4,2,0].stutter(2), oct=4, dur=[1,1,2])

b2 + (0,2)

b1.amplify=pa64
b2.amplify=pa32_2

b_all.root=var([0,-3,0,2],16)
b_all.crush = var([0,4,8,16],8)

d8 >> play("/", dur=16)

d2.every(14, "stutter", 4, dur=3)
d2.every(14, "stutter", 8, dur=6)

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)

e2 >> play("t{n.}", dur=cascara, sample=P[0,1,2].stutter(4), amplify=po32_3)

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)
e3.amplify=po16_2

e4 >> play("funky", amp=2, rate=4*PRand([1,1.5,1.25]), dur=1/2, pan=PStep(6,P*(-1,1)))

################################################################

b1.dur=2
b1.oct=5

chords = var([0,5,2,3],[8,4,2,2])

b1.fadeout()

bb >> hpluck(chords, dur=PSum(3,2), oct=4, amp=.7, amplify=pa32)
v1 >> vibra(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4, pa32_2)

v1 + var([(0,2),(2,4)],[28,4,16,16])

l1.fadeout()

v1 + P*(0,2)
v1 + P*(0,2,0,-3)
v1 + P*(0,2,0,-3)
v1 + P*(0,2,0,4,0,-3)

c1 >> nlead([0,2,4,-1,0], dur=clave23, oct=5, amplify=po32)

d1 >> kicker("<hHh ><f >", dur=cascara, amp=PWhite(.8,1.2)[:17])
