
################################################################

b1 >> crubass(
    PWalk(seed=3)[:17],
    dur=1,
    # sus=.6,
    oct=[2,3,(2,3)],
    **rndp(crubassp, 1),
    # **rndp(phaserp, 4),
    amp=1,#PWhite()[:17],
    # pan=sinvar([-1,1], 16),
    # reverb_dw=.6,
)

k1dur = zipvar([
    # (P[2/3],16),
    (P[1],16),
    # (P[4/3],16),
])
k1 >> kicker(
    [(6,5)],
    dur=k1dur,
    amp=sinvar([.2,.8], [5,7,9,2,7])
)

################################################################

Clock.bpm=160

d3deg = zipvar([
    ('xxo[-o][-o]xo[-o]',15),
    ('[oo]x',1),
    ('xxo[-o][-o]xo[-o]',14),
    ('[xx][ox]',2),
    ('xxo[-o][-o]xo[-o]',14),
    ('<ooxo>< = =>',2),
    ('xxo[-o][-o]xo[-o]',12),
    (' ',4),
])
d3 >> play(
    d4deg,
    dur=1/2,
    # sus=1/2,
    amp=var([1,0], [56,8]),
    sample=3,
    resob_dw=0,
    vol=.4,
)

################################################################

b2 >>  tb303(
    [0,0,4,0,0,2],
    dur=1/4,
    sus=1/2,
    pan=sinvar([-1,1], 16),
    tb303_i_freq=linvar([.1,.7],16),
    tb303_i_reso=linvar([.7,.1],7),
    tb303_i_decay=linvar([.3,.6],12),
    tb303_i_delay=linvar([.1,.5],7),
    reverb_dw=linvar([.1,.5],12),
    amp=var([0,1], [8,56]),
)

b2 >> tb303(0, dur=1/4, sus=1, oct=[2,3,4,5])


b2 >> danceorg(
    [0,0,1],
    dur=1/4,
    sus=4/5,
    oct=[2,3,4,5],
    amp=[.9]*5+[0]+[.9]*7+[0]*2,
    reverb_dw=.4,
    root=var([0,4,2,0], 8)
)

b1 >> balafon(
    0,
    dur=cascara*4,
    oct=Pvar([[6],[5]], 3),
    amp=Pvar([PWhite(.7,.9)[:17],[0]],[6,2]),
    delay_vol=.5,
    pan=sinvar([-1,1],16),
    vol=1,
)

################################################################

b1 >> balafon(
    PWalk()[:65],
    dur=var([1/4, 1/3, 1], 8),
    oct=(5,6,7),
    amp=var([1,0],[6,2]),
    delay_vol=.5,
    pan=0,#sinvar([-1,1],16),
    vol=1,
)

b7 >> bass([0,2], dur=1/2)
print(b7.sus)

b1 >> crubass(PWalk()[:65], dur=1/4, oct=3, sus=1/2)

################################################################

d1 >> kit808(
    P["x--(-[--])o--(=-)"].layer("mirror"),
    pan=sinvar([-1,1],8),
    dur=gnawa*2,
    rate=var([1,4],[28,4])
).every(5,'stutter', 0)

################################################################

k1 >> kicker(
    P[0,2,4],
)

tt >> metronome("(ttt=) o o o ", dur=1/2)
