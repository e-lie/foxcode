

p1deg = zipvar([
    (P(0,2,4),4),
])
p1dur = zipvar([
    (cascara*4,8),
    (1/3,8),
])
p1 >> bells(
    p1deg,
    dur=p1dur,
    sus=1,
    # amp=sinvar([.2,1], [5,7,9,2,7]),
    # reverb_dw=.2,
    # reverb_dw=expvar([0,.6],17),
    **rndp(bellsp, 12),
    oct=[6,7],
)

b4deg = zipvar([
    ([0,2,3],16),
    ([0,2,0],8),
])
b4dur = zipvar([
    (cascara*4,16),
])
b4 >> bells(
    b4deg,
    dur=b4dur,
    sus=3,
    oct=5,
    **rndp(bellsp, 13),
)
