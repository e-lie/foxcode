
from FoxDot.preset import *


rhythms = {
"half" : P[1/2],
"swing100" : P[4/10,6/10],
"swing" : P[3/10,7/10],
"square" : P[1/4,3/4],
"triplet" : P[1/3],
"binlet" : P[1/2,1/4,1/4],
"cubalet" : P[4/10,3/10,3/10],
"binlet2" : P[1/4,1/2,1/4],
"gnawa" : P[3/10,4/10,3/10],
"quarter" : P[1/4],
"brazlet" : P[3/10,1/5,1/5,3/10]*2,
"brazlet100" : P[1/3,1/6,1/6,1/3]*2,
"quintuplet" : P[1/5],
"brafflet" : P[3/12,2/12,2/12,2/12,3/12,2/12]*3,
"clave" : P[3/15,3/15,4/15,2/15,3/15]*bar_length,
"clave23" : P[3/16,3/16,4/16,2/16,4/16]*bar_length,
"cascara" : P[2/16,2/16,1/16,2/16,1/16,2/16,1/16,2/16,2/16,1/16]*bar_length,
}

trésillo = PSum(3,8)/2
cinquillo = PSum(5,8)/2

print(PEuclid(3,8))

b1 >> blip(0, dur=1/4, amp=PEuclid(5,16), oct=[6,4,5])
b2 >> bbass(4, dur=1/4, amp=PEuclid(11,16), oct=[3,4])
d1 >> play("-*", dur=cascara)
d2 >> play("v", dur=1)

b1.amplify = var([1,0],[24,8])
b2.amplify = var([1,0],[12,8,12])
d1.amplify = var([1,0],[16,4])
d2.amplify = var([1,0],[12,4])

@player_method
def pause(lenght, total, shift):
    pass

b_all.crush=linvar([2,16], 16)
b_all.sus=sinvar([.1,2,.3,1,.7,.1], [4,5,12])

b1 >> blip(0, dur=cinqu)

bembé = PSum(7,12)/2
venda = PSum(5,12)/2

bossa = PSum(5,16)/4
bossacomp = PSum(11,16)/4

samba1 = PSum(7,16)/2
samba2 = PSum(9,16)/2

print(bembé)

################################################################

Clock.bpm=140


k1 >> play("(Xxxx)-", sample=0, dur=1, amp=1.5)
k1 >> play(" -", sample=0, dur=1, amp=1.5)
k2 >> play("s", sample=0, dur=cascara, amp=.3)
bb >> bbass([0,0,-2,-1,0,2,-1], dur=clave23, oct=3)
nn >> blip([3,2,0,-2,0,1], dur=.25, sus=.2, amp=[.2,.6,.8,0,1,0,1,.8], amplify=2).mpan(mrot(18)) + [0,[0,2,4],0,P*(-2,0)]

###

b1 >> blip([0,0,-2,-1,0,2,-1], sample=0, dur=cascara, amp=.8)
b2 >> pluck([0,0,-2,-1,0,2,-1], dur=clave23, oct=4)
b3 >> blip([0,0,-2,-1,0,2,-1], dur=1/4, oct=7, amp=.7).stop()

################################################################

d1 >> play("+", sample=1, dur=bembé, amp=3)
k2 >> play("+", sample=0, dur=venda, amp=3)
k3 >> play("-", sample=0, dur=1/4, amp=.8)

################################################################

k1 >> play("(Vx.x)(xxV)", sample=3, dur=clave23, amp=1.5).mpan(0)
d1 >> play("+", sample=1, dur=samba1, amp=3).mpan(mrot(32)+2)
k2 >> play("s", sample=0, dur=samba2, amp=P[2].stutter(4)|P[0], crush=16, bits=8).mpan(mrot(32))

k3 >> play("-", sample=0, dur=cubalet, amp=2, crush=linvar([0,16],16), bits=8).mpan(mrot(64)+2)

################################################################

change_bpm(120)

b1 >> marimba([0,0,-2,-1,0,2,-1], sample=0, dur=samba1, amp=.8)
b2 >> marimba([0,0,-2,-1,0,2,-1], dur=samba2, oct=4)
b3 >> blip([0,0,-2,-1,0,2,-1], dur=.25, oct=7, amp=.7)
b4 >> blip([0,0,-2,-1,0,2,-1], dur=1, oct=3, amp=4) + [0,[0,2,4],0,P*(-2,0)]

b4 >> blip([0,2,0], dur=cubalet, oct=7, amp=2).stop(1.5)
b4 >> blip([0,2,0,2,-2,-5], dur=cubalet, oct=7, amp=2).stop(1.5)
b4 >> blip([0,2,0,2,-2,-5], dur=cubalet, oct=7, amp=2)
b4 >> blip([0,2,0,2,-2,-5,-8,-12,-60,-62,-62,-65], dur=cubalet, oct=7, amp=2).stop(1.625)
b4 >> blip([0,2,0,2,-2,-5,-8,-12,-160,-162,-162,-165], dur=cubalet, oct=7, amp=2)
b4 >> blip([0,2,0,-162,-2,-5,-8,-12,-160,-162], dur=cubalet, oct=7, amp=2) + var([0,2,-5],2)

Root.default = var([0,0,2,0,4], 16)

Scale.default = Scale.egyptian
