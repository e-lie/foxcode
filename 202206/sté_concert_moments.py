from FoxDot.preset import *

sc >> supercollider()
change_bpm(60)
Scale.default = Scale.minor

f1 >> fordrip(0, dur=PRand(1,4), oct=PWalk(7,1,3)[:17])
f1.faderand()

m1 >> madg(PStutter([0,2], [1,2,3,1]), dur=2, scale=Scale.minor, oct=4)


d7.faderand()

d6 >> crazykit("www.", dur=cubalet)
d5 >> crazykit(" (HHH[HH]H[HHH])", dur=.5, amp=.6)

Clock.bpm = linvar([60,100], [16,8,24,16], Clock.mod(4))

f2 >> whibot2(PWalk(7,1,3)[:17], dur=PRand(1,4), oct=6)
f2.faderand()

bpm_to(100, 16)
change_bpm(100)

################################################################

change_bpm(120)

sc >> supercollider()

m1 >> tb303(
    P[0,2,4,-5,2],
    dur=cascara,
    root=var([0,2,0,4], [16,8,8,16,8]),
    scale = Scale.minor,
    oct = 3,
)

Scale.default = Scale.minor

bb >> blip([0], root=var([0,4,-5,0,2], PRand(0,4)[:16]), dur=.25, scale=Scale.minor)
bb.stop()

sc >> supercollider(verb_w=linvar([.6,1], 8), verb_size=linvar([.8,1], 16))

tt >> play("X(---[--])", sample=(0,1), amp=[1.2,.8])
dd >> ducker(0, sus=.5, ducking=.4)
t3 >> play(".(...(.(*[**]*)))", sample=(0,1), amp=[1.2,.8], room=3, dur=.5, sus=4)

t2 >> play("<VxxVx>< (*[**]) >", dur=clave23, sample=P[0,1,2].stutter(4))

t5 >> play("t{t.}", dur=cascara, sample=P[0,1,2].stutter(4), amplify=pa32_3)
t6 >> play("n", dur=clave23, sample=P[0,1,2].stutter(4), amplify=pa32, pan=P[-1,0,1].stutter(2))
t7 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=po16_3, pan=var([-1,0,1],2))




################################################################

Scale.default = Scale.minor

change_bpm(160)

b1 >> darkpass([0,2,1,-1], oct=4, dur=4)
b_all.root=var([0,-3,0,2],16)
b2 >> bbass(P[4,2,0].stutter(2), oct=4, dur=[1,1,2])
b2 + (0,2)
b1.amplify=pa64
b2.amplify=pa32_2
b_all.room = sinvar([0,4], 16)
b_all.crush = var([0,4,8,16],8)
# d1 >> play("<X ><V >", dur=.5, sample=2, amplify=pa32)

d2 >> play("<v.O..vo.>", dur=.5, sample=0, rate=linvar([.8,1.2], 16), amp=.8)
d2.every(14, "stutter", 4, dur=3)
d2.every(14, "stutter", 8, dur=6)

d2.sample=var([0,1,2], 32)

d3 >> play("<(-~)[--]>", dur=.5, amplify=pa32_3)
d4 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], pan=[-1,0,1], amplify=pa16_3)

c1 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)
c1.amplify=po16_2

b1.dur=[2,4,1,2,3]
b1.root=var([0,-3,0,2],16)
b1.amplify=pa32_3

d2.stop()

t5 >> play("t{n.}", dur=cascara, sample=P[0,1,2].stutter(4), amplify=pa32_3)

d5 >> play("funky", amp=2, rate=4*PRand([1,1.5,1.25]), dur=1/2, pan=PStep(6,P*(-1,1)))

p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1,0,1), sus=4, bits=8, crush=8) + (0,8)

d8 >> play("/", dur=16)

################################################################

change_bpm(110)


b1 >> tb303([0,0,2,-5,0,-2], oct=3)
b1.dur = swing100*2

d3 >> crazykit("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

d8 >> play("/", dur=16, sample=0)

k1 >> kicker("<hHh ><f >", dur=cascara, amp=PWhite(.8,1.2)[:17])

################################################################

chords = var([0,5,2,3],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,2,2,4])

bb >> hpluck(chords, dur=PSum(3,2), oct=4, amp=.7)
l1 >> nlead(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4)
l1 >> marimba(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=chords.dur, oct=4)
l2 >> marimba(chords + [[2,0,0],0,[0,2,2],[0,0,2]], dur=clave23, oct=4)

pp >> vibra2([0,2,4,7,8,2], dur=1/2, sus=1/2, amplify=pa16_2, pan=-1) + [0,0,[0,0,1]]
l1.amplify=pa32

l1 + var([(0,2),(2,4)],[28,4,16,16])

l2 + var([(0,2),(2,4)],[28,4,16,16])

l2 + P*(0,2)
l2 + P*(0,2,0,-3)
l1 + P*(0,2,0,-3)
l1 + P*(0,2,0,4,0,-3)

d7 >> ceramic2([0,2,4,1,2,2,4,-5], dur=clave23, oct=4)

d8 >> play("/", dur=16, sample=0)

k1 >> kicker("<hHh ><f >", dur=cascara, amp=PWhite(.8,1.2)[:17])

vv.fadein()

################################################################

c1 >> chicad([0,2,4], dur=cascara)
