from FoxDot.preset import *


d1 >> play("ooo.o.ooo", dur=cubalet, sample=1, amp=.8)
d2 >> play(" -", dur=.5, sample=2 , amp=3)

d4 >> play("<V >", dur=.5, sample=2)

d3.stop()

b1 >> wobblebass([0,2,4], scale=Scale.minor, dur=2, oct=(3,4))
b1.amplify=pa32
b1.root=var([0,2,-5,0], 16)

################################################################

m1 >> marimba([0,2,6,7,2,4], dur=1/3, root=var([0,2,-5], 4),
    scale=Pvar([Scale.minor, Scale.egyptian], 32), oct=var([4,5,6,7], 8))

m2 >> marimba([0,2,-5], dur=cubalet, root=var([0,2,-5], 4), oct=4,
    scale=Pvar([Scale.minor, Scale.egyptian], 32))

m3 >> vibra([0,2,-5], dur=clave23, root=var([0,2,-5], 4), oct=5,
    scale=Pvar([Scale.minor, Scale.egyptian], 32))

m4 >> blip([4], dur=.25, amplify=pa16_2)
m2 >> blip([12], dur=.25, amplify=pa16)
m3 >> blip([12,0], dur=clave23, amplify=pa16, oct=(2,4,6))
m1 >> blip([12,0], dur=1/3, amplify=pa32, oct=(2,4,6))


m1 >> blip([12,0], dur=1/3, amplify=pa32, oct=(2,4,6))

m2 >> blip([12,0], dur=.25, amplify=pa32, oct=(2,4,6))

m3 >> blip([12,0], dur=clave23, amplify=pa32, oct=(2,4,6), crush=linvar([0,32], [32,0]))
m3.amp = PRand(1)[:17]
p1 >> play("V ")

m3 >> blip([12,0], dur=[.4,.3,Rest(.3)], amplify=pa32, oct=(2,4,6), crush=linvar([0,32], [32,0]))
m4 >> blip([12,0], dur=cascara, amplify=pa32, oct=P(2,3), crush=linvar([0,32], [32,0]))

m4 >> twang([12,0], dur=.5, amplify=1, oct=P(2,3), crush=linvar([0,32], [32,0]))
