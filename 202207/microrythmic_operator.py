from FoxDot.preset.common import *
from FoxDot.preset.reaper import *

p1 >> play("VT", dur=P[.5]<<[0,-.25,0,0])
p1 >> play("VT", dur=P[.5])


p2 >> play("-", dur=P[.5,.25,.25]<<[0,linvar(),.1], amp=2) # cubalet

[.4,.3,.3]

Clock.bpm = 110

################################################################

p1 >> play("XT", dur=[2-var([1,.5, .5], [2,4,1]),var([1,.5], [2,2,1])])

dur1 = P[.5]<<[0,0-var([.25,0],4),0,0]
p1 >> play("vi", dur=dur1)

dur2 = P[.5,.25,.25]<<[0,var([.1,.08,.04,0],4),var([.05,.04,.02,0],4)]
p2 >> play("X", dur=dur2, amp=PWhite(.8,1.2)) # cubalet

################################################################

C = var([0,4,3,2,0,-5],[4,4,2,2,2,2])
b1 >> marimba(C, dur=dur1, oct=3, amp=PWhite(.8,1.2))
b2 >> marimba(C, dur=dur2, oct=5, amp=PWhite(.8,1.2))

b3 >> blip(C, dur=dur2, oct=5, sus=.5, amp=PWhite(.8,1.2))

b1 + [[0,2],[-2,0,0],[4,0,(0,-5)]]
b2 + [[0,2],[-2,0,0]]

b_all.sus = None

Scale.default=Scale.egyptian

p1 >> play("vi", dur=dur1)
