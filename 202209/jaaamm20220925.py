

b1 >> blip([num/40 for num in range(400)], dur=.125, sus=sinvar([0.1,.7], 7), crush=0, oct=PRand([3,5,6]))

b2 >> space([num/40 for num in range(400)], dur=1/9, sus=sinvar([0.1,.7], 7), crush=0, oct=PRand([6,4,7]))

b3 >> play("[VV]-[--]-x[---]--v", dur=1, rate=PRand([1,.8,1.5]), crush=sinvar([0,16]))

b4 >> play("X (O[ooo]O)  X(OO[OO][*O]) ", sample=2, crush=8, amp=1.2, rate=var([1,2], 8))

Clock.clear()
4

d1 >> play(
    "-",
    dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25] << P[0] | PRand([0,.05,.08])[:9],
)

d2 >> play(
    "*",
    dur=P[.75,.75,1.0,.5,1.0]
)

Clock.bpm=100
