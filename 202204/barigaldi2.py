k1 >> kicker(
    # "a",
    "<a><d  A>",
    # dur=.5,
    dur=.25,
    amp=PWhite(.6, 1.2)[:17],
    # shim=0,
    amplify=pa16,
    shim=.8,
)
k1.span(rotrand1)
k1.fadein(16)
dk >> ducker(0)

d1 >> kicker(
    degree="<d   a>",
    # degree="www ",
    # degree="<www ><b (   B)>",
    dur=clave23,
    #dur=clave23,
    vol=1.5
)
d1.span(rotrand2)
# d1.solo()
# d1.

k1.every(8, "stutter", 2)
# k1.vol=0

b1 >> crubass(
    # degree=PRand(0, 5)[:16]*2,
    degree=P[0, 0, 2, 1],
    dur=PSum(3, 5),
    # scale=Scale.minoratonic,
    reso=sinvar([0, 1], 16),
    cutoff=linvar([0, .3], 30),
    root=P[0, 3, 4].stutter(16),
    oct=2,
    amplify=pa32_2,
).span(rot16)

c1 >> ceramic(
    PTri(0, 8, 2).stutter(2),
    # dur=.25,
    dur=cascara,
    root=P[0, 3, 4].stutter(16),
    # oct=P[2, 3].stutter(8),
    oct=PRand(2, 8),
    # oct=P[2, 3, 4].stutter(3),
    # amplify=pa16,
    reverb_wet=sinvar([0, 1], 17)
).span(rotrand2)
# c1.fadein(16)
# c1 + (2, 4)
# c1 + (2, 4, 6, 8)

c1.root = PTri(0, 32, 2).stutter(4)
c1.dur = 0.125

c1.sfadeout(32)
c1.only()

c1.fadeout()

Clock.clear()

d4 >> play("<* ><ww[oo] >", dur=cascara).mpan(range(6))
# d4.fadein(16)
d4.formant = [0, 1, 2]
d4.rate = PWhite(.1, 10)[:17]
