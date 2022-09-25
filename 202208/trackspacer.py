from FoxDot.preset import *

Scale.default = Scale.minor

d1 >> play("<V.><x.>", output=10, amp=.7, rate=.9, sample=(0,3))

b1 >> tb303([0,0,0,2,-2], output=12, oct=3, dur=cascara)

s3 >> sc3().span(srot(32))
s2 >> sc2().span(srot(32))

b1.root = var([0,2,0,-2,0,4])
b1.amp = linvar([.4,1], [32,16])
