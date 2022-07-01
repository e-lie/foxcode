from FoxDot.preset import *



Root.default=var([0,2,0,-3], 8)

Scale.default = Scale.majorPentatonic
Scale.default = Scale.egyptian
Scale.default = Scale.minorPentatonic
Scale.default = Scale.minor

Root.default=var([0,1,2,-1,-3], 8)

p1 >> marimba([0,1,2,4,5,2,3,0], dur=.5, amp=linvar([.4,1.2], 2), sus=linvar([.25,1], 8)).humz()

p1.amp = linvar([0,1.2], 4)

p1.oct = 3
p1 + [0,(0,2),(0,-3),0]
p1.every(2,"reverse").every(5, "stutter", 2).every(17, "stutter", 4)

p2 >> bbass([0,1,2,3], dur=1, amp=linvar([.4,1.2], 2), sus=linvar([.25,1], 8))
p2.every(17,"reverse").every(3, "stutter", 0)
p2 + (0,2,4)
