from FoxDot.preset import *


d1 >> play("Vvvv", dur=.25, sample=0, amplify=pa32).mpan(range(6))
d1 >> play("(VVVX)( v)(vvvx)(v )", dur=.25, sample=0, amplify=pa32).mpan(range(6))

d2 >> play("(VVVX)( v)(vvvx)(v )", dur=.25, sample=0, amplify=pa16).mpan(P[range(6)].stutter(3))

d2 >> play("<.-><(   ( = (*[**])))>", sample=P[0,2,3,4].stutter(2))

d3 >> play("(TTT*)(ttooTT)(-=-T)", dur=Pvi([1/3],[1/2,1/4,1/4], 16), amplify=pa16, sample=0)

d4 >> play("*** ", dur=cascara, amplify=pa16, sample=2)


################################################################

d1 >> play("Vvvv", dur=.25, sample=var([3,0], 16), amplify=pa32).mpan(range(6))
d2 >> play("(VVVX)( v)(vvx)(v v[VV])", dur=.25, sample=var([1,2], 32), amplify=pa16).mpan(P[range(6)].stutter(3))
d5 >> play("VVvV.", dur=clave23, sample=var([2,3], 16)).mpan(drot32)

d_all.amp=pa64

d3 >> play("--.---.-.----..--", dur=cascara, amp=3).mpan(4)

b2 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.majorPentatonic).mpan(drot(17))
b2.fmod=var([0,32],[24,8])
b2.amplify=pa16_2

b1 >> blip(PRand(0,11)[:17], dur=.25, scale=Scale.majorPentatonic, oct=7).mpan(drot(17))
b1.fmod=var([0,128],[28,4])
b1.amplify=pa16

b_all.fadein()

################################################################


b1 >> marimba(P[0,0,4,2,-5, 0, 2], dur=cascara, amplify=pa32) + [0,P(2,-5)]
b2 >> marimba(P[0,0,4,2,-5, 0, 2], dur=.333333, amplify=pa16_2, oct=[5,6,7], scale=Scale.minor) + [0,.5]
b3 >> vibra(P[0,0,4,2,-5, 0, 2], dur=.333333, amplify=pa16, oct=[3,4]) + [0,(.5,0)]

b2.span(linvar(rot16))

################################################################

b3 >> marimba(P[0,0,4,2,-5, 0, 2], dur=Pvi([1/3],[1/2,1/4,1/4], 16), amplify=pa16*1.2) + [0,P(2,-5)]
b3.root = var([0,2,0,4], 32)

b4.root = var([0,2,0,4], 16)
b4 >> vibra(P[0,0,4,2,-5, 0, 2], dur=.3333333, amplify=pa32*.5, oct=4) + [0,P(2,-5)]


################################################################


b3 >> vibra(P[0,0,4,2,-5, 0, 2], dur=[2,3,2,4], amplify=pa32*.5, oct=4) + [0,P(2,-5)]
b4 >> vibra(P[0,0,4,2,-5, 0, 2], dur=P[2,3,2,4].shuffle(), amplify=pa16*.5, oct=6) + [0,P(2,-5)]
b5 >> vibra(P[0,0,4,2,-5, 0, 2], dur=P[2,4,2,3], amplify=pa16_2*.5, oct=5) + [0,P(2,-5)]
d4 >> play("-(- - )-( = -)", dur=.25, amplify=pa16, sample=2).mpan(P[range(6)].stutter(3))


################################################################

b3.span(rot16)
v2.span(rotrand1)

v1 >> vibra([0,1,2,3,4], dur=clave23) + [(1,3),(0,4)]
v2 >> marimba([0,1,2,3,4], dur=cascara) + P*(0,4)
d1 >> play("xx.x.xx", dur=cascara).mpan(P[range(6)].stutter(4))
d2 >> play("Vv", dur=clave23).mpan(P[range(6)])

d3 >> play("--.-", dur=cascara).mpan(2)


m1 >> marimba([0,1,2,3,4], dur=brafflet*4)
m2 >> marimba([0,1,2,3,4], dur=1, oct=4) + [0,2,4]
m3 >> vibra(PWalk()[:17], dur=cascara, oct=5)
m_all.scale = Scale.egyptian

################################################################

mallets = Group(m_all, v_all, a_all)

m1 >> marimba([0,2,2,3,0,2], dur=[4/10,4/10,4/10,3/10,3/10,2/10], oct=P[5,6].stutter(2))
m2 >> marimba([0,2,2,3,0,2], dur=[4/10,4/10,4/10,3/10,3/10,2/10], oct=P[4,3].stutter(2))

a1 >> marimba([0,2,2,3,0,2], dur=1/3, oct=P[5,6].stutter(2))
a2 >> marimba([0,2,2,3,0,2], dur=1/3, oct=P[4,6].stutter(3)).span(rot16)

m_all.stop()

mallets.only()

m1.degree=[0,0,4,0]

mallets.scale=Scale.egyptian

Root.default = var([0,2,4], 3)

m1 + P(0,4,11)

m_all.amplify=pa16
a_all.amplify=pa16_2m1.stop()


################################################################

change_bpm(110)

d1 >> play("V-(...\)", dur=1/3).mpan(drot32)
d2 >> play("t(..tT)").mpan(drot32)
d3 >> play("XxxXx.", dur=cubalet).mpan(drot32)

################################################################

l1 >> loop("foxdot", dur=4)

################################################################

n1 >> pads([4,4,2,6], dur=4, oct=4, amp=3)
