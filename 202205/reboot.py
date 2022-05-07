from FoxDot.preset import *

p1 >> play(
    "<   X><o o ><---->",
    rate=linvar([.5, 1.5], 17),
    sample=var(range(4), 4),
    amp=PWhite(.2, 2),
    dur=PWhite(.4, .6)[:17],
    se
    # dur=linvar([.2, .8], 64),
).mpan(range(6))

p2 >> play("* *o *** *oo* **o*o ", sample=[3], rate=linvar([2, 6], 17))
p2.dur = cubalet
# p2.mpan()
p2.mpan([3, 4])

p3 >> play(
    "<Xxvv><v   >",
    dur=.25,
    amp=[2, 1, 1, 1],
    rate=linvar([1, 2], 128),
    fmod=32
)
p3.mpan(P[range(6)].stutter(4))
# p3.mpan(0)

b1 >> bass([0, 0, 2, 3], dur=2, oct=5).mpan([0, 1])

b2 >> blip(
    [0, 0, 2, 3],
    dur=cascara,
    oct=6,
    root=[0] * 8 + [2] * 12,
    amp=PWhite(2, 4),
    fmod=P[64, 128].stutter(4),
).mpan(range(6))

tt >> play("o").mpan(range(6))
