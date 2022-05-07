p1 >> play("X ").mpan(1)

p2 >> play("<[--]><**o*>", sample=2).mpan(P[range(6)].stutter(3))
p1 >> play("<[.o].......><     (*[**])          >").mpan(1)
p3 >> play("Vvvv", dur=.25).mpan(3)
p2.amplify = pa32
p5.stop()
b1 >> blip(PRand(7), root=var([0, 2, 4], 16), dur=.25,
           oct=var([4, 5, 6], 32)).mpan(P[range(6)].stutter(4))

b1.dur = Pvar([.25, 1], [24, 8])
p5 >> play("oooo", dur=cascara, sample=2).mpan(4)

d1 >> bass([0, 0, 2, 3], scale=Scale.minor, dur=4).mpan(0)

d1.root = var([0, 2, 3], 32)

p4 >> play("TTTTT ", dur=cubalet, sample=0).mpan(4)


@nextBar(16)
def up16():
    p4.humz()


@nextBar(32)
def up32():
    p3.sample = var([0, 1, 2], 64)


@nextBar(64)
def up64():
    p3.only()
