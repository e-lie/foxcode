from FoxDot.preset import *



Scale.default = Scale.chromatic

b2 >> blip(var([0,12,11,10]), dur=PWhite(.1,.3), oct=[7,8,9], slide=0).pause(4,32).stop()


b1 >> pluck(var([0,12,11,10]), dur=.25, sus=3, oct=[3,4], crush=var([0,8,64],7)).pause(24,32,13).stop()


b3 >> bbass([0,-1,-2,-3,-4], dur=8, sus=16, oct=var([3,4], 17), amp=0)

d1 >> play("[----]-[--]-=-=-=", crush=0, rate=linvar([1,4],7))


d5 >> play("v[vv]vv[vvvvv]", dur=1/3, rate=1, amp=.6)

d3 >> play("==[==]==[=***-]", dur=var([1,1/2,2,1/3]), rate=PWhite(1,3), amp=PWhite(0,2), sample=PRand(1,3))


d3 >> play("==[==]==[=***-]", dur=var([1,1/2,2,1/3]), rate=PWhite(1,3), amp=PWhite(0,2), sample=PRand(1,3))


d4 >> blip(P[range(100)]/10, crush=var([0,8,64],7), dur=.1, sus=PWhite(.1,3), oct=7, amp=0).pause(16,32,13).ampfadein()
