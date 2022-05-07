from FoxDot.preset import *

t3 >> fmsaw(
    "Aa bbB",
    oct=(2, 6),
    dur=cubalet * 2,
    reverb_w=0,
    scale=Scale.minorPentatonic,
    # vol=linvar([.5, 1], 16),
    # pan=linvar([-1, 1], 7),
    root=var([0, -5, 2, 4], 2),
    #amp=[1] * 8 + [0] * 2 + [1] * 1,
).fadein(16)

t2 >> vital2(
    [0, 2, 4],
    oct=2,
    reverb_w=sinvar([0, 1], 16),
    vol=linvar([0, 1], 16),
    pan=linvar([-1, 1], 7)
)

t1.stop()

change_bpm(160, True)

p1 >> play(
    "<X-o--Xo-><(...*)(*.*.)..><...(...[xo])>",
    # amp=[1] * 8 + [0] * 2 + [1] * 1,
    pan=[-1, .5, 1, 0] * expvar([0, .8], 32),
    sample=[2] * 3 + [1] * 2,
    output=2,
)

pp >> sca(
    vol=1,
    pan=0,  #expvar([-1, 1], 4),
)

ggg = Group(t3, p1, pp)

pp.amp = linvar([0, 1], 16)

p1 >> prophet([0, 2, 0, 1], output=2).stop()

p2 >> marimba(
    "abcaca",
    oct=var([3, 4], 16),
    root=var([0, 4, 2, -5], 4),
    output=2,
    amp=PWhite(1, .6)[:187],
    dur=cubalet * 2,
    scale=Pvar([Scale.major, Scale.minor], 6),
    reverb_wet_amount=0,
    reverb_decay_time=2,
    reverb_room_size=2,
    vol=sinvar([0, 1], 16),
)

p3 >> marimba(
    "abac",
    oct=var([2, 3], 16),
    root=var([0, 4, 2, -5], 4),
    output=2,
    amp=PWhite(1, .6)[:187],
    dur=P[3, 1, 2, 2] * 2,
    scale=Pvar([Scale.major, Scale.minor], 6)
)

p1.fadein(32)
pp.fadein(32)

t3.fadein(32).stop()

ggg.fadeout(16)
