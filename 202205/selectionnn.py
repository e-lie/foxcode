from FoxDot.preset import *

d1 >> play("Vvvv", dur=.25, sample=var([3,0], 16), amplify=pa32).mpan(range(6))

d2 >> play("(VVVX)( v)(vvx)(v v[VV])", dur=.25, sample=var([1,2], 32), amplify=pa16, sdb=0).mpan(P[range(6)].stutter(3))

d5 >> play("VVvV.", dur=clave23, sample=var([2,3], 16)).mpan(drot32)
d5 >> play("VVvV.", dur=cascara, sample=var([2,3], 16)).mpan(drot32)

d5.solo()

d1 >> play("<Vvv(v-v[VV])><  - >", dur=.25, sample=2, output=2)

b1 >> wobblebass([0,2,4], scale=Scale.minor, oct=P(3,4,5), root=var([(0,4),(0,2)], 16), dur=2)

d_all.amp=.8

print(clave23)

d_all.amp=pa64

d_all.amplify = 1

d7 >> play("--.---.-.----..--", dur=cascara, amp=3, verb_w=0).mpan(mrot(17))
d7 >> play("--.---.-.----..--", dur=cascara).mpan(mrot(17))
d7.amplify=1
d7.verb_wet=0

d3.fadeinout(16,16)

b2 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.minor).mpan(mrot(17))
b2.fmod=var([0,32],[24,8])
b2.amplify=pa16_2

s1 >> pink([0,2,4], amp=.3)

s2.stop()



b1 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.majorPentatonic, oct=3, amp=3).mpan(mrot(17))
b1.fmod=var([0,128],[28,4])
b1.amplify=pa16

b1.only()

b1.mpan(var([0,2,4], 4))

b1 + P(0,4,12)
# b1.fadeout()
b1.dur=cascara
b1.degrade()

b3 >> blip(PRand(0,11)[:17], dur=clave23, scale=Scale.majorPentatonic, oct=P[2,(7,3)].stutter(5), amp=3).mpan(mrot(17))
b3.fmod=var([0,128],[28,4])
b3.amplify=pa16

b1.root=var([0,2,0,-5], 4)

b_all.fadeout()

b2 +(0,4)

b2.sfadeout()

b3 >> nlead([0,2,4], dur=clave23)

k1 >> kicker("GH", dur=.25, vol=1)
k3 >> kicker("GH", dur=clave23, vol=1)

g3 >> bass([0,0,2,3], dur=PSum(5,3))
g3.stop()

k2 >> play("* * ", amp=4)

b3.stop()

d2.fadeinout(8,4)
d5.fadeinout(8,4)
d1.fadeinout(16,32)
d5.fadeinout(16,32)


d_all.fadeout()
d_all.stop()

b_all.fadein()

b_all.root=var([0,2,4,6], 8)

b_all.scale=Scale.egyptian

b3 >> wobblebass([0,0,1,4,0], dur=4, oct=2)

d2 >> play("<X(X.XX.)><-[--]>", sample=PRand(0,4)[:13], rate=linvar([0.5,2], 16), crush=linvar([0,32], 32))

d2.fadeout()

################################################################

b2 >> tb303([0,2,4,6], dur=.25, oct=(2,3), root=var([2,-5,0,0,4,0,3,2], 2))


################################################################

s2 >> noise(PWalk()[:77], dur=.25, sus=1, amp=.7, scale=Scale.chromatic, oct=3)
s3 >> play('<V   >< (-------[--])>', sample=2, rate=PWhite(.5,2)[:17], dur=.5)
# s5 >> play('-', sample=2)
s4 >> blip([0,2,3], scale=Scale.minor, dur=1/6, oct=6, root=var([0,-1,2,-5,4,0,2], 1))
s4 >> blip([0,2,3], scale=Scale.minor, dur=P[1/2,1/3,1/3,2/3]/2, oct=6, root=var([0,-1,2,-5,4,0,2], 1))
