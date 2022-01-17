

s1 >> owstr(
    P[0,2,4],
    dur=[4,3,5],
    root=var([0,2,4,5,0],16),
)

s1.only()

b2 >> bells(
    P[0,2,4],
    dur=cubalet*,
    sus=1/2,
    oct=[5,5,6,6,7,8],
    vol=.7,
    **rndp(bellsp, 7),
).only()

d2deg = zipvar([
    "",
])
d2dur = zipvar([
    (P[1],16),
])
d2 >> jazzkit(
    [0,4,12],
    dur=cubalet*2,
    sus=.1,
    reverb_dw=.2,
    resob_dw=,
    vol=.7,
)
