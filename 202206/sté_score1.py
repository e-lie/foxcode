from FoxDot.preset import *

sc >> supercollider()
sv >> sverb()
change_bpm(100)

Scale.default = Scale.majorPentatonic

Root.default = 0

m1 >> marimba([3,2,-2,0,2], )

# Root.default = var([0,2,-5], 64)
#
#
#
# chords = var([0,2,-3,1,0],[8,4,8,4,8])
#
# m1 >> marimba(chords, dur=cascara, oct=3)
# m1 + var([P*(0,3), 0, [0,2]], chords.dur) + (0,2,4)
# m2 + var([P*(0,1), 0, [0,2]], chords.dur) + (0,2,4)
#
# m3 >> blip(chords, dur=cascara, oct=7) + [(0,2),0,(2,0)]
# m3 + var([(0,2),(2,4)],[28,4,16,16])


m1 >> marimba('<ab(dadD) ABD >', dur=cascara, oct=3)
m2 >> marimba('(aG) ', dur=clave23, oct=[6,7,5]).every(8, "stutter", 3)
m3 >> marimba('<cC >', dur=cascara, oct=3)
m4 >> blip('<h h h h>', dur=cascara, oct=5)

Root.default = var([0,1,3], [3,7,9,12])

k1 >> kicker("(f)", ssc=1, amp=1.2).stop()
k2 >> kicker("aba ", ssc=1, amp=1.2, dur=cascara)

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

d1 >> crazykit("<bB(bBb )><Ss >", dur=cubalet).humz()
d1.stop()
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

b1 >> owstr([0,2,-5,2,4,0], dur=4, root=var([0,4,2,-5],8))
b1.amplify=var([.8,0], [24,8])

# play with params

################################################################

b1.dur= Pvar([swing100*4,4],16)

d1 >> kit808("H ", dur=cascara, amp=1.2)
d2 >> kit808("w", dur=clave23, amp=.9).humz()

k1 >> kicker([0,9], oct=3, ssc=.8, dur=1).every(16, "stutter", 3)

b1 >> crubass([0,0,2,-5,0,-2], oct=3, dur=[2,2,1,3])
b1.fadein(16)

# play with params

d2.amplify = d1.amplify = var([1,0],[48,16])

d1.degree = Pvz([
    ("H ", 16),
    ("H(hhH) ", 16),
    ("Hh", 16),
])

b1.dur = swing100*2
b1.sus = swing100*2 - 0.03

mi.phaser_dw=.6

d1.reverb_dw = sinvar([0,.5],16)

d2.fadein(16)

d3 >> kit808("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])
d3 >> crazykit("sss ", dur=var([.25,.125],[12,4]), amp=PWhite(.6,1.1)[:17])

d4 >> play("/", dur=16, output=2)

k1 >> kicker("<aAc ><C >", dur=cascara, amp=PWhite(.8,1.2)[:17], ssc=.8)

b1.fadeout(16)

b1 >> bbass([0,0,2,-5,0,-2], oct=4)
b1.dur = swing100*2

change_bpm(110)

k1.fadeout()

b1.fadeout()

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

c1 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)
c1.amplify=po16_2

b1.dur=[2,4,1,2,3]
b1.root=var([0,-3,0,2],16)
b1.amplify=pa32_3

d2.stop()

t5 >> play("t{n.}", dur=cascara, sample=P[0,1,2].stutter(4), amplify=pa32_3)

d5 >> play("funky", amp=2, rate=4*PRand([1,1.5,1.25]), dur=1/2, pan=PStep(6,P*(-1,1)))

p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1,0,1), sus=4, bits=8, crush=8) + (0,8)


################################################################

chords = var([0,5,2,3],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,4,2,2])
chords = var([0,-4,-3,2],[8,2,2,4])

bb >> hpluck(chords, dur=PSum(3,2), oct=4, amp=.7)
bb >> bbass(chords, dur=PSum(3,2), oct=4, amp=.7)
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
