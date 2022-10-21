from FoxDot.preset import *

change_bpm(120)

vibra, marimba = add_chains("vibra", "marimba")
candy, bass303 = add_chains("candy", "bass303")

b1 >> bass303([0,0,4], dur=cascara, bass303_reso=linvar([0,1], 16))
d1 >> play("V-", dur=Pvar([.5,cascara],[24,8]))

m1 >> marimba(0, dur=var([.125, .7, 2,1],3), oct=var([4,6],3), amp=PWhite(.7,.8), amplify=linvar([0,1.5])).span(srot(16)).pause(4,16)

m3 >> marimba(0, dur=Pvar([1/3,cascara],16), amp=PWhite(.7,1), amplify=linvar([0,1.5]), oct=3).pause(4,16)

m2 >> candy(0, dur=clave23, oct=4, sus=linvar([.1,.5], 16)).span(srot(16))

m3 >> candy(0, dur=cascara, oct=[8,6,7], sus=linvar([.1,.5], 16))

d2 >> play("(v[VV]v[vvv]V)(---[--]*[**])", dur=1/2, crush=var([0,16,4,32]), rate=PWhite(.1,2.5)).mpan(var([0,3])).pause(8,32, 12)
d2 >> play("V-", dur=1/2, crush=var([0,16,4,32]), rate=PWhite(.1,2.5)).mpan(var([0,3])).pause(8,32, 12)

d1 >> play("oo.oooO.", dur=clave23, crush=0, rate=PWhite(.1,1)).mpan(var([0,3])).pause(6,32)

d3 >> play("OO[OOO]o.OO.", dur=cascara, crush=0, rate=PWhite(1,2)).mpan(var([0,3])).pause(6,32,4)



print(candy)
