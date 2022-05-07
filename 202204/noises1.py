from FoxDot.preset import *

p1 >> fordrip([0, 0, 17]).span(linvar([0, 5.9], [8, 0]))

b1 >> accciddd([0, 2, 4], dur=4, oct=3).span(rotrand1)

b1.ampfadein(16)

p1.showp()

p2 >> play(
    "ooo  wws ss ss",
    dur=cascara,
    #amp=1,
    rate=linvar([.2, 2, .1], 16),
    formant=sinvar([0, 4], 7),
).mpan(PRand(0, 6)[:77])

p3 >> play(
    "Vx",
    crush=3,
    formant=sinvar([0, 1], 17),
    dur=Pvar(
        [
            clave23,
            [1],
            # [8]
        ],
        8
    )
).mpan(range(6))

print(clave23)

b1 >> bass(
    [.1, .2, 3, 2.7],
    root=var([0.1, 0.8]),
    oct=var([5.1, 4.8], 16),
    scale=Scale.chromatic,
    fmod=expvar([0, 8], 32)
).mpan(range(6))

p4 >> play(
    # "o.o.o..o.oo.ooo.oo.oooo",
    "o",
    dur=Pvi(
        cascara,
        cascara,
        # PWhite(.25, .5)[:10],
        32
    ),
    sample=0,
    # sample=var([0, 1, 2, 3], 3)
).mpan(var([0, 2, 1, 5, 3, 0, 4], 5)).stop()

p5 >> play(
    # "o.o.o..o.oo.ooo.oo.oooo",
    "w",
    dur=Pvi(
        cascara,
        # cascara,
        [.4] * 10,
        # PWhite(.25, .5)[:10],
    ),
    sample=[0],
    # sample=var([0, 1, 2, 3], 3)
).mpan(var([0, 2, 1, 5, 3, 0, 4], 4))

print(cascara)

change_bpm(120)

t1 >> marimba(
    "<ab[cbc]d[ed][fe]><[fe]c>",
    dur=P[.55, .45] + PWhite(-0.02, 0.02)[:17],
    root=var([-5, 2, 0, 4], 3),
    oct=[2, 5],
    scale=Scale.minorPentatonic,
)

t2 >> play(
    "o(h )sO( H  )[ss]",
    amp=[.8, .9, .7, 1],
    dur=P[.4, .3, .3] * 1.5 + PWhite(-0.02, 0.02)[:17],
    sdb=[0, 1],
).mpan(range(2))
