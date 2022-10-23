from FoxDot.preset import *

Scale.default = Scale.majorPentatonic
Root.default = var([0,-2,-5,-4])

p1 >> bbass(P[0,2,1,-2,-1], dur=PSum(3,2), oct=4).pause(8,16)

p2 >> blip(P[0,2,1,-2,-1], dur=P[.5,1], sus=P[.5,1,1.5], oct=P[3,6,3,7]).pause(8,16,4)

p3 >> blip(P[0,2,1,-2,-1], dur=cascara, sus=P[.5,1,1.5], oct=8).pause(4,16,12)

d1 >> play("<(["+"X"*3+"]x(X[XX])).><*v>", dur=clave23)

d2 >> play("*.**[**]=", dur=cascara)

d2 >> play("i", dur=cascara, amp=.3)

Jules Cipher
