

from FoxDot.preset import *


Scale.default = Scale.majorPentatonic

p1 >> play("(XxvV)(..-[--])", dur=cascara)

p1 >> play("(   v)(--(i[ss]s)(si[--]))", dur=cascara).mpan([0,4,0,2,0,5,0,3])

p2 >> play("< vxV><II >", dur=clave23).mpan([1,4,2,5])

p3 >> bbass(0, oct=3, dur=cascara, root=var([0,2,-3], [2,4,8,2])) + Pvar([P(0,4), P*(0,2)], 8)

p4 >> marimba([0,2,1,-2], oct=6, dur=.25, root=var([0,2,-3], [2,4,8,2])) + [(0,4),(0,-3)]

p4.span(srot(16))

p3.mpan(var([0,3,1,4,2,5],4))

p_all.crush=expvar([0,64], 32)
p_all.bits=linvar([4,64], 37)
p_all.rate=expvar([.6,1.5], [2,15,7,4,8])

Clock.bpm = 125

Clock.link()

p1 >> play("Vi")

print(Clock.bpm)

change_bpm(120)
