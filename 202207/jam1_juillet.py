from FoxDot.preset.reaper import *

p1 >> play("VIi", dur=P[.4,.3,.3]*2, room=0)
p2 >> play("VIVi", dur=1, room=0)
p3 >> play("--", dur=.25, room=0)

p_all.sample=var([0,1,2,3], 4)

b1 >> bbass([0,0,0,7], dur=PSum(3,2), oct=(2,3), crush=32)
b2 >> marimba([0,0,0,7], dur=PSum(3,2), oct=P*(2,3,4,5,6,7,8), crush=32)

p1.amplify=pa64
p2.amplify=pa64
p3.amplify=pa64_2
