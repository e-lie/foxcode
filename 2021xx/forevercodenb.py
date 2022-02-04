


bb >> mixer()
change_bpm(120)
Scale.default = 'minor'

p1 >> harshkit(
    "absfd ",
    dur=Pvi(triplet, binlet, 64),
    amp=[1, .6],
    sample=1,
    **fadein(),
    # hamp_dw=.9
)

p1 >> karp(0)

Player.get_attributes()

p1 >> piano(
    # degree=[0, 2, 4],
    # root=Pvar([0, 3, 4, 2], 4),
    **Pzr(
        [
            ([0, 2, 4], 0, 4),
            ([0, 2, 4], 4, 4),
            ([0, 2, 4, 4, 4, 0], 3, 4),
            ([0, 2, 4], 5, 4),
        ]
    ),
    dur=Pvi(triplet, binlet, 64),
    amp=[.6, .8],
    # sample=1,
    # resob_dw=.3,
    phaser_dw=.6,
    hamp_dw=linvar([0, .9], 64, start=Clock.mod(4)),
)

# d3 >> play("*", dur=1/4, sample=1, amp=.5 )
d3 >> play(
    "*",
    sample=2,
    dur=Pvi([1/4], [.1, .4], 32),
    amp=PRand(1)[:16],
    pan=[-1, 0, 1],
)

d3.solo()

d4 >> play("V", dur=1, sample=1, amp=.8)

d1 >> kit808("x    x  ")
d2 >> kitdatai("  o   o ", resob_dw=.3, amp=.7)
d3 >> kit808("  s   soso      ", dur=1/4, reverb_dw=.4, amp=.4)

change_bpm(180)
d1 >> play(
    "<X    X  ><V    V  ><  o   o >",
    sample=PRand(3)[:16],
    room=3,
    reverb_dw=.7
)

d3 >> kitdatai("  s   soso      ", dur=1/4)
d4 >> kitdatai("-", dur=1/4, sample=PRand(3)[:7], room=3, amp=.8)

b1 >> crubass(
    [0, 0, 2, 3],
    dur=[2],
    **rndp(crubassp, 12),
    oct=[2, 3],
    root=var([0, 4, 3, 0, 2, 4], 8),
    vol=1,
)

d3.degree = "  s   sosos  sos"
d3.amp = [.8, 1, .6, 1]
d1.amp = 1
