sc >> supercollider()

change_bpm(100, True, .81)
change_bpm(100)

Scale.default = Scale.minorPentatonic
Root.default = 0


f1 >> fordrip(-20, dur=8).fadein(32)

d1 >> play("ii[II]", dur=clave23, sample=[2,3], pan=[-1,(-1,1),1], room=2)

m1 >> marimba("ab[ddcf][ccdd]", oct=[3,6]).humz()
m2 >> marimba("b[ddcf][ccdd]afedc", oct=[4,5]).humz()
m3 >> marimba("b[ddcf][ccdd]afedc", oct=[6,2]).humz()


m1 >> marimba("aba([c]a[cccc]d)[ff]", oct=[3,4,3,5], amplify=pa32).humz().span(srot(17), .8)

m2 >> blip([5,2,3,2], dur=.25, pan=[-1, 0, 1], amp=2).humz()

Root.default = var([0,5,-2], 32)

M = var([(0,2),(2,3)],[8,4,2,2])

m3 >> marimba2(M + [[2, 0, 0], 0, [2, 2]], dur=cascara, oct=P[5,4,7].stutter(4))

m3.amplify = pa32_3

d2 >> play("iI", dur=cascara, sample=[0,1], pan=[-1,(-1,1),1], room=4)

m3.every(8, "reverse")

Scale.default = Pvar([Scale.majorPentatonic, Scale.minorPentatonic], 32)


m1.every(16, "reverse")

m2 + P*(0,2)

k1 >> play("Vi")


m2 + P*(0,3)

m3.fadeout()
m2.fadeout()

m1.fadeout()

m2.stop()
bb >> blip(P[0,2,-3,4].stutter(8), dur=.25, sus=sinvar([.25,1],16), oct=(4,6), pan=P[-1,0,1].stutter(2))

bpm_to(120, 16)

change_bpm(120, True, .81)

Scale.default=Scale.minor
Root.default = 0

bb >> blip(P[0,2,-3,4].stutter(8), dur=.25, sus=sinvar([.25,1],16), oct=(4,6), pan=P[-1,0,1].stutter(2))

f2 >> whibot2(PWalk(7,1,3)[:17], dur=PRand(1,4), oct=6)

f2.faderand()

b1 >> tb303([0,2,4,-5,2], dur=var([.5, 1/3], [24, 8]), sus=sinvar([.25,2],16), oct=(4,6), pan=P[-1,0,1].stutter(2))

b1.only()

Root.default = var([0,2,4,0],[16,8,8,16,8])

d3 >> play(".*[**].", rate=var([1,2]))

k2 >> play("X", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, pan=[-1, 0, 1])

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2)

d1.amplify=po16

b2 >> bbass([0,2,4,-5,2], dur=cascara, oct=5) + P(0,2)

d3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), amplify=pa16_3, pan=var([-1,0,1],2))

b2.degrade()

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)
