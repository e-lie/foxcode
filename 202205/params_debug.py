from FoxDot.preset import *


v2 >> vibra([0,2,3], root=var([0,-5,-6,2], 16), dur=cascara, amp=pa32).span(srot(8))


v2.verb_width=

v2.showp("verb_dry")


c1 >> ceramic(sus=.5, oct=[3,5,7], dur=clave23*2) + P*(0,2,4)
c1.span(rotrand1)
c1.ceramic_tone = linvar([0,1], 7)

c1.showp("macro")


l1 >> strpad(dur=8).span(rotrand1)

d1 >> play("V ")
