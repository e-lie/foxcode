




@meta(m1)
p1 >> piano1

d1 >> play("X-  X -")

m1 >> meta("4/4", 32, 128)

p1 >> crubass(var(range(32),1, start=Clock.mod(4)), dur=.25, oct=2, amp=expvar([.5,1,0], [32,.2,inf], start=Clock.mod(4)))
