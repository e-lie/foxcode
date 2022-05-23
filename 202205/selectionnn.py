from FoxDot.preset import *

d1 >> play("Vvvv", dur=.25, sample=var([3,0], 16), amplify=pa32).mpan(range(6))
d2 >> play("(VVVX)( v)(vvx)(v v[VV])", dur=.25, sample=var([1,2], 32), amplify=pa16).mpan(P[range(6)].stutter(3)).fadein()

d5 >> play("VVvV.", dur=clave23, sample=var([2,3], 16)).mpan(drot32)

d1 >> play("Vvv(v-v[VV])", dur=.25)

print(clave23)


d_all.amp=pa64

d_all.amplify = 1

d3 >> play("--.---.-.----..--", dur=cascara, amp=3, verb_w=0).mpan(mrot(17))
d3.amplify=1
d3.verb_wet=0

d3.fadeinout(16,16)

b2 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.majorPentatonic).mpan(mrot(17))
b2.fmod=var([0,32],[24,8])
b2.amplify=pa16_2



b1 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.majorPentatonic, oct=3, amp=3).mpan(mrot(17))
b1.fmod=var([0,128],[28,4])
b1.amplify=pa16

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
