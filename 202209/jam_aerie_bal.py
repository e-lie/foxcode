from FoxDot.preset import *

Root.default = var([0,4], 16)

Scale.default = Pvar([Scale.minor, Scale.egyptian], 16)

b1 >> bell([0,2,4,6,8], dur=[.125], sus=.2, crush=0, oct=[5,6,7,8]).mpan(range(6)).pause(24,32)

p1 >> play("*", dur=cascara).mpan(range(6)).pause(4,32,17)

p2 >> blip([0,1,2,3,4], dur=.25, sus=linvar([.1,2],9),  crush=0, oct=var([7,8])).pause(4,16).mpan(range(6)).ampfadein()

d1 >> play("v  [xx]", crush=linvar([0,64],16)).mpan(range(6))

d2 >> play("<*iiv[**i*][*I]><V >", dur=cascara, crush=linvar([0,8],16)).mpan(5).pause(8,16,7).ampfadein()

d3 >> play("V", dur=clave23, sample=PRand(0,4)).mpan([3,5]).pause(0,24).solo()

p4 >> pluck([0,12], dur=.125).mpan(range(6))

p5 >> bbass([0,2,3, 0,2,5], dur=PSum(3,2), amp=.7, oct=3).mpan(3)
p7 >> bbass([0,2,3, 0,2,5], dur=PSum(5,3), amp=.7, oct=5).mpan(5)

p5.solo()


b1 >> pluck(0)
