from FoxDot.preset.reaper import *
from FoxDot.preset.common import *

################################################################

change_bpm(110)

Scale.default = Scale.majorPentatonic
Root.default = 0


f1 >> fordrip(-20, dur=8).fadein(16)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=6, amp=sinvar([.1,.9],32), dur=.125)

m1.span(var([0,4,2], 8))

m2 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=5, amp=sinvar([.1,.9],17), dur=.125, ).humz()

m2.span(var([1,3,2], 8))

m2.dur=.125


Scale.default = Scale.egyptian
m1.degree = "ab([c]a[cccc]d)[ddd][cc]a....b[aaaa][ff]"
m2.degree = "ab([c]a[cccc]d)[ddd][cc]a....b[aaaa][ff]"

Scale.default = Scale.minor


Scale.default = Scale.chromatic



m3 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=[4,5,6,7,8], amp=linvar([.5,.9],7), dur=cascara).humz()

m1.dur=clave23
m2.dur=1

m4 >> blip([5,2,3,2], dur=.25, pan=[-1, 0, 1], amp=1.5).humz()

m4.sus=expvar([.1,1], 16)

d1 >> play(" (---[ *])", amp=1.5)
dd.rate = sinvar([.7,1.8], 23)

f2 >> fordrip2((-20,0,10,40), dur=PRand(1,4), oct=PWalk(7,1,3)[:17])


m1.solo()
m1.solo(0)

d1 >> play("-", dur=1/3, sample=PRand(0,4)[:77])

Root.default = var([0,5,-2], 32)

d1 >> play("-", dur=Pvar([clave23, 1/3, 16], 16), sample=PRand(0,4)[:77], pan=[-1,(-1,1),1], rate=P[-.7,1,1.4].stutter(4))

m2.dur=0.125
m1.dur=0.1
m1.dur=clave23

m1.solo()
m1.solo(0)

m1 >> marimba("aba([c]a[cccc]d)[ff]", oct=[3,4,3,5], amplify=pa32).humz()

m1.span(srot(17), .8)

m2 >> blip([5,2,3,2], dur=.25, pan=[-1, 0, 1], amp=1.5)

M = var([(0,2),(2,3)],[8,4,2,2])

m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4))

m3.amplify = pa32_3

# d1 >> play("i", dur=clave23, sample=[2,3], pan=[-1,(-1,1),1], room=4)


m3.every(8, "reverse")

Scale.default = Pvar([Scale.majorPentatonic, Scale.minorPentatonic], 32)

m1.every(16, "reverse")

m2 + P(0)

k1 >> play("v ")
k1 >> play("<V ><X >")
k1 >> play("V(i  i i [ii] i[ii])")
k2 >> play("v", dur=cascara)
k2 >> play("V-", dur=.5)

m2 + P*(0,3,2)

m3.fadeout()
m2.fadeout()

m1.only()



################################################################

l1 >> loop("200173-breakbeat5.wav", 0, rate=[1.35, 1.35, -1.35, -2.7], dur=4)
l1 >> loop("200173-breakbeat5.wav", 0, rate=[1.35, 1.35, -1.35, -2.7], dur=4, )
l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=[1.35, 1.35, -1.35, -2.7], dur=[4,2,2, 1, 1, 1, 1])

l2 >> loop("200173-breakbeat5.wav", [0,0,2,2,0], rate=[1.35, 1.35, -1.35, -2.7], dur=[4,4,1,2], pan=-1)

d1 >> play("^^^ ", dur=clave23, sample=3, slide=[-2,4], rate=[.5,1,-.5])
d2 >> play("^", dur=cascara, sample=3, slide=[-2,4], rate=[2,3,-2])
d3 >> play("^-", dur=.5, sample=3, slide=[-2,4,1], rate=[.4])

################################################################

Clock.bpm=162

dd >> play("<V(---([==][--]))>< ( [ o] [ o]  [o ] )>")
dd >> play("<V(---([==][--]))>< ( [ o] [ o]  [o ] )>", rate=linvar([-1,-.2,.2,1],[16,0,0,48]), slide=0)

Clock.link()

################################################################

p1 >> play("Vi(I[ii][ I][ i])(VV[vv])", dur=clave23)
p2 >> play("Vi(I[ii][ I][ i])(VV[vv])", dur=cascara)

p_all.rate = 1
p2.rate = sinvar([-1,1], [4,16])
p1.slide = P[-.5,2,.5,0,0].stutter(10)

bb >> tb303(Pvar([[0,2,4,8],[2,-2,0,0]], [24,8]), oct=3, crush=0, dur=Pvar([PSum(3,2),1/4], [24,8]))

################################################################

change_bpm(120)
Clock.bpm=120

d1 >> play("i(iIi[**]i[ii]i)(iii[ii])", dur=brafflet, amp=PWhite(.7,1)[:17]*linvar([.8,1.2], 16)).humz()
d1 >> play("i", dur=brafflet, amp=PWhite(.7,1)[:17]*linvar([.8,1.2], 16)).humz()
d1 >> play("V-", dur=brafflet, amp=PWhite(.7,1)[:17]*linvar([.8,1.2], 16))
d2 >> play("v (v[ v])( I)v (   [--])", dur=.5).humz()
d2 >> play("I I [I]  ", dur=.5).humz()
d2 >> play("V x [X]  ", dur=cascara)

d3 >> play("V-", dur=clave23)
d5 >> play("T", dur=cascara)
d4 >> play("v-", dur=.5)

d1.rate = PWhite(.8,1.4)[:17]
d2.slide = PWhite(0,-1)[:17]

bb >> tb303([0,2,3,4,-3,2,0], dur=.5, oct=3) + P*(0)
b2 >> tb303([0,2,3,4,-3,2,0,-2,4,2], dur=.5, oct=6) + P*(0)

b_all.crush=linvar([1,16], 4)

bb.mpan(mrot(16))

print(sum(brafflet*4))

################################################################

d1 >> play("V-", dur=brafflet, amp=PWhite(.7,1)[:17]*linvar([.8,1.2], 16))
d3 >> play("v-", dur=clave23)
d4 >> play("X-", dur=.5)

sc >> supercollider()

b2 >> blip([0,1,-2,4], dur=brafflet, oct=6)
b1 >> blip([0,1,-2,4], dur=.25, oct=7)

bb >> darkpass([0,2,1,-1], oct=4, dur=8, amplify=pa64)

Root.default=0

b1.dur= Pvar([.25, brafflet], [24,8])

d_all.sample = var([0,1,2], 16)

e8 >> play("/", dur=16)
e8.mpan(mrot(32))

d_all.rate = PWhite(.7,2)[:17]

d_all.slide = PWhite(-2,2)[:32]


d_all.mpan(range(6))

d_all.mpan(mrot(16))
b1.mpan(mrot(8))
b2.mpan(mrot(24))

d1.amplify = pa32
d2.amplify = pa32_2
d3.amplify = pa16

k1 >> play("^", amp=3, rate=2.5, dur=cubalet, amplify=po16)
k2 >> play("^", amp=3, rate=4, dur=1/3, amplify=po16_2)


################################################################

change_bpm(120)

d1 >> play("i", dur=brazlet)
d2 >> play("I", dur=cubalet)
d3 >> play("V-", dur=.5)

m1 >> vibra(0, dur=brazlet)
m2 >> vibra(2, dur=cubalet)
m3 >> vibra(4, dur=.5)

d_all.amp=.6
d_all.degrade()

################################################################

square = P[1/4,3/4]

varswing = Pvar([.5, swing100, swing, square, swing, swing100],8)
varswing2 = Pvar([.5, swing100, swing, square, swing, swing100],7)
varswing3 = Pvar([.5, swing100, swing, square
, swing, swing100],13)

b1 >> blip([0,1,2,4,1,0,-3,-1], dur=varswing, oct=[5,6])
b3 >> blip([0,1,2,4,1,0,-3,-1], dur=varswing2, oct=[6,5,7])
b4 >> blip([0,1,2,4,1,0,-3,-1], dur=varswing3, oct=6)

b1.pan =-1
b2.pan = 1
b3.pan = 0

b2 >> blip([0,1,2,4,1,0,-3,-1], dur=.25, oct=1) + (var([0,1,2,3,4],1),var([12,11,10,9,8], 4), var([4,5,6], 7))

b2.oct=2

Root.default=var([0,2,4], [1,2,4,8])

Scale.default=Pvar([Scale.egyptian, Scale.minor], 4)

Scale.default=Scale.majorPentatonic

print(sum(brafflet*3))

b1.sus=var([.1,.5,2], 2)
b2.sus=var([.1,.5,2], 4)
b3.sus=var([.1,.5,2], 7)
b4.sus=var([.1,.5,2], 3)

################################################################
