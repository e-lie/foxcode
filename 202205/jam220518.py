from FoxDot.preset import *


m1 >> marimba([0,2,3], dur=.25, root=var([0,2,-5], 8))

m1.verb_wet = 1

m1.fadeout()

m1.sur_x = 0

m1.span(rot16)

################################################################

b1 >> blip([0, 4], oct=P[4,5,6].stutter(2), dur=gnawa, amp=pa16) + (0,2)
b1.mpan(mrot(32))

b2 >> blip(P[0].stutter(3), oct=var([4,7],4), dur=1/3, amp=pa16_2) + P*(0,2,4)

b3 >> blip([0,2,4,-5], oct=var([4,7],4), dur=1, amp=pa16_2, root=var([0,2,3], 16)) + P(0,6)

b3.sfadeout()

b2.stop()

d1 >> play("<Vvvv><   (---=)>", dur=clave23, amp=.7, amplify=pa32, sample=var([0,1], 8)).mpan(mrot(17))
d1 >> play("<(---=)>", dur=clave23, amp=.7, amplify=pa16_2, sample=var([0,1], 8)).mpan(mrot(17))
d4 >> play("<(---=)>", dur=cascara, amp=.7, amplify=pa16, sample=var([0,1], 8)).mpan(mrot(17))
d3 >> play("<o><  [**]>", dur=cascara, amp=.7, amplify=pa32, sample=var([0,1,2], 8))
d3.degrade()

d2 >> play("<(X[VVV]XX[Vxx]) >", dur=.25, amp=.7, amplify=pa32, sample=var([0,1], 8)).mpan(mrot(7))

d2.sfadeout()

d3.only()

t2 >> bass([0,0,2,4], dur=PSum(3,5), oct=5, amp=.8, root=var([0,2,3], 16)).mpan(mrot(16))

t2.sfadeout()

d2.only()



################################################################

Scale.default = Pvar([Scale.minor, Scale.egyptian, Scale.majorPentatonic], 16)

v2 >> vibra([0,2,3], root=var([0,-5,-6,2], 16), dur=cascara, amp=pa32).span(srot(8))
v1 >> vibra([0,2,3], root=var([0,-5,-6,2], 16), dur=clave23, oct=4, amp=pa16_2) + (0,4)
v3 >> vibra([0,2,3], root=var([0,-5,-6,2], 16), dur=1, oct=3, amp=pa16) + [0,2,4]

d1 >> marimba("TT ", sample=var([0,2], 4), amplify=pa32, dur=.5)
d2 >> vibra([0,2], sample=var([0,2], 4), amplify=pa16, dur=1/3) + (0,-5)

d3 >> marimba(PWalk()[:17], sample=var([0,2], 4), amplify=pa16, dur=.25) + (0,2)

d3.span(rot16)
d2.span(srot(12))

d_all.solo()
marimba

d4 >> play("V ")

#####################################################("---###########

d1 >> play("*(   [**])  ", dur=.5, sample=var([0,2,1], 4)).mpan(mrot(17))

d2 >> play("*", amp=2, dur=.5).mpan(range(6))


################################################################
