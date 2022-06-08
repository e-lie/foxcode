from FoxDot.preset import *

change_bpm(120)

m1 >> tb303([0,2,4,-5,2], dur=cascara, amp=PWhite(.1,.9), root=var([0,2,0,4], [16,8,8,16,8]), verb_w=1, verb_size=linvar([.8,1],8))

sc >> supercollider(verb_w=linvar([.6,1], 8), verb_size=linvar([.8,1], 16))
