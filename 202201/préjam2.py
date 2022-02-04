rchange_bpm(130, True)
bb >> mixer()

Scale.default = "major"
Root.default = 0

base = P[4, 0, 4, 2, 0, 0]

m1 >> bells(
    (base, 8),
    dur=cubalet,
    **rndp(bellsp, 7),
    **fadein(16, 0.8),
    reverb_dw=0.5,
    oct=[4, 5, 6, 5, 6, 5],
    # oct=Pvar([[4, 5, 6, 5, 6, 5], [7, 6, 5, 3, 5, 7]], [24, 8]),
    pan=sinvar([-1, 1], 3),
)

p6 >> piano(interpolate([1/3, 1/3, 1/3], gnawa))

m1.amp = PWhite(.5, 1)[:17]

d3 >> kit808("www", dur=cubalet, amp=[1, 0.8], root=0, **fadein())


d3.degree = "wwwww "
d3.amp = Pvar([[1, 0.8], 0.5, 0], [24, 2, 6])
d3.degree = "<wwwww ><-->"

s1 >> owstr([0, 4, 2, -1], dur=16, oct=7, **fadein(16, fvol=0.8))

k1 >> jazzkit(
    "<---- ---- - ><* >",
    dur=gnawa,
    amp=[1, 0.6, 0.8],
    pan=sinvar([-0.5, 0.5], 8),
    root=0,
    **fadein(8, 0.7),
)

s2 >> owstr([0, 4, 4, 3, -1, 2, -1], dur=8, oct=3, vol=0.9, **ampfadein(16))

k1 >> jazzkit(
    "<---- ---- - ><* >",
    dur=gnawa,
    amp=[1, 0.6, 0.8],
    pan=sinvar([-0.5, 0.5], 8),
    root=0,
    **fadeoutin(16, ivol=0.8),
)


m1 >> bells(
    (base, 8),
    # (base, 19),
    # oct=[7, 6, 5, 3, 5, 7],
    dur=cubalet,
    **rndp(bellsp, 8),
    reverb_dw=0.5,
    **fadein(4, 1, 0.8),
    # vol=sinvar([.2,.9],16),
    oct=[4, 5, 6, 5, 6, 5],
)

Root.default = var([4, 0, 3, -1, 2, -2, 1, 0], 4)

d2 >> kicker(
    (5, 11),
    # **fadein(16, 0.7),
    vol=.9,
    reverb_dw=0,
    dur=Pvar([[1/2], [1], 17]),
    root=0,
    # **delay(subdiv=1 / 3, feedback=0.9),
)

m1.degree = zipvar(
    [
        (base, 24),
        (base + 12, 8),
    ]
)
m1.amp = [0.8] * 11 + [0]

d3 >> play(
    "<  (ew)l><=><funky>",
    rate=4 * PRand([1, 1.5, 1.25]),
    dur=1 / 4,
    amp=.8,
    pan=PStep(7, P * (-1, 1)),
)

k1 >> jazzkit(
    "<---- ---- - ><* >",
    dur=gnawa,
    amp=[1, 0.6, 0.8],
    pan=sinvar([-0.5, 0.5], 8),
    root=0,
    **fadeout(16),
)

m1 >> bells(
    (base, 8),
    # (base, 19),
    # oct=[7, 6, 5, 3, 5, 7],
    dur=cubalet,
    **rndp(bellsp, 8),
    reverb_dw=0.5,
    **fadeout(32),
    oct=[4, 5, 6, 5, 6, 5],
)

s2.only()

# Clock.bpm=sinvar([130,140,150],32, start=Clock.mod(4))

change_bpm(140, True)
# Root.default = 0
Scale.default = Scale.minor

d1 >> kitdatai(
    "< ([--]=)->< s><(      [ox]) >",
    dur=cascara * 4,
    # oct=3,
    **fadein(16),
    root=var([4, 0, 3, -1, 2, -2, 1, 0], 4),
    resob_dw=sinvar([0.1, 0.5], 16),
    pan=expvar([-1, 1], 4),
)

d1.stop()

b1 >> crubass(
    [0, 2, 4, 0, 2, 3],
    # root=var([0, 4, 0, 0, 5, 4], 16),
    oct=2,
    dur=PSum(12, 7),
    sus=PSum(12, 7) - 0.03,
    # vol=1,
    **fadein(24, .7),
    # sus=4,
    **rndp(crubassp, 5),
)

b1.stop()

d1 >> play(
    "<  (ew)l><=><funky>",
    rate=4 * PRand([1, 1.5, 1.25]),
    dur=1 / 4,
    **ampfadeout(32),
    pan=PStep(7, P * (-1, 1)),
)

d2 >> kicker(
    (6, 5, 11),
    amp=var([1, 0], [56, 8]),
    reverb_dw=0.3,
    **fadein(16, 0.9),
    # vol=.6,
)

s2.stop()

b2 >> tb303_2(
    [0, 0, 4, 0, 0, 2],
    dur=1 / 4,
    pan=sinvar([-1, 1], 16),
    # vol=0.8,
    **fadein(32, 0.6),
    tb303_i_freq=linvar([0.1, 0.7], 16),
    tb303_i_reso=linvar([0.7, 0.1], 7),
    tb303_i_decay=linvar([0.3, 0.6], 12),
    tb303_i_delay=linvar([0.1, 0.3], 7),
    reverb_dw=linvar([0.1, 0.5], 12),
    amp=var([0, 1], [8, 56]),
)

d2 >> kicker(
    [(6, 5, 11)] * 3 + [(14, 10)],
    amp=var([1, 0], [56, 8]),
    reverb_dw=0.3,
    **fadein(16, 0.9, 0.6),
    # vol=.6,
)

d3 >> play("*", sample=2, dur=1 / 4, amp=PRand(2)[:16], pan=[-1, 0, 1])

d1.amp = linvar([1, 0], [16, inf], start=Clock.mod(4))


b2.stop()
m1 >> bells(
    (base, 8),
    # (base, 19),
    # oct=[7, 6, 5, 3, 5, 7],
    dur=1 / 4,
    **rndp(bellsp, 2),
    resob_dw=expvar([0.2, 0.5], 7),
    reverb_dw=0.5,
    **fadein(16, 0.8),
    oct=[4, 5, 6, 5, 6, 5],
)

s1 >> pulse(PWhite(32), dur=1 / 4, fmod=10, oct=5, **ampfadein(16))
s1.amp = var([1, 0], [24, 8])

d3.stop()
# replace kicker
d2 >> play("<Vn><  u >", sample=[0, PRand(7)]).every(6, "stutter", 4, dur=3)
# d2.stop()

b2 >> tb303_2(
    [0, 0, 4, 0, 0, 2],
    dur=1 / 4,
    pan=sinvar([-1, 1], 16),
    # vol=0.8,
    **fadein(16, 0.9, 0.6),
    tb303_i_freq=linvar([0.1, 0.7], 16),
    tb303_i_reso=linvar([0.7, 0.1], 7),
    tb303_i_decay=linvar([0.3, 0.6], 12),
    tb303_i_delay=linvar([0.1, 0.3], 7),
    reverb_dw=linvar([0.1, 0.5], 12),
    amp=var([0, 1], [8, 56]),
)

change_bpm(143, True)
change_bpm(148, True)
change_bpm(155, True)

s1 >> owstr([0, 4, 2, -1], dur=16, oct=7, **fadein(16, fvol=0.8))
s2 >> owstr([0, 4, 2, -1], dur=8, oct=3, vol=0.9, **ampfadein(16))

d3 >> kit808("www", dur=cubalet, amp=[1, 0.8], root=0, **fadein())
d3.degree = "wwwww "
d3.amp = Pvar([[1, 0.8], 0.5, 0], [24, 2, 6])
d3.degree = "<wwwww ><-->"

d3.stop()

d2 >> play("<Vn><  u >", sample=[0, PRand(7)], **ampfadeout(32)).every(
    6, "stutter", 4, dur=3
)


rooooottt = P[4, 0]
descente = Pattern()
for i in range(100):
    descente = descente | rooooottt-i
descente += 15
m1.only()
Clock.bpm = linvar([155, 30], [32, inf], start=Clock.mod(4))
m1 >> bells(
    (base, 8),
    # (base, 19),
    # oct=[7, 6, 5, 3, 5, 7],
    dur=1 / 4,
    **rndp(bellsp, 2),
    root=descente,
    resob_dw=expvar([0.2, 0.5], 7),
    reverb_dw=linvar([.2, 1], [32, inf], start=Clock.mod(4)),
    **fadeout(32),
    oct=[4, 5, 6, 5, 6, 5],
)


Clock.clear()

d4 >> play("<funky><  (ew)l>", rate=4
           * PRand([1, 1.5, 1.25]), dur=1/2, pan=PStep(6, P*(-1, 1)))
Clock.bpm = 50
