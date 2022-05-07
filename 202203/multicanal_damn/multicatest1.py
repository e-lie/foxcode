from FoxDot.preset import *

d2 >> play(P[" - (-- )"].bubble(), output=[4], pan=[-1])
d3 >> play(P["  o(o )"].bubble(), output=[6], pan=[-1])
d1 >> play(P["x(   x)   "].bubble(), output=[2], pan=[1])
d4 >> play(P["T"], output=[2], pan=[-1], dur=P[4/10, 3/10, 3/10] * 2)
d5 >> play(P["s"], output=[4], pan=[1], dur=[.4, .3, .3])
d6 >> play(P["X "].bubble(), output=[6], pan=[1])

dd >> play("X", output=4, pan=[-1, 1])

d1 >> play("X", **mpan(P[range(6)] + .5))
d1 >> play("X", **mpan(range(6)))
d1 >> play("X", output=[6], pan=[-1, 1])

d3 >> play("XXX XX X", **mpan(range(6)), dur=1, sample=var([0, 1, 2], 3))
d1 >> play("s ss s s", **mpan(range(6)), dur=cascara, amp=2)
d2 >> play("ww w wwww w", **mpan(range(6)), dur=clave23, amp=1)
# d2 >> play("XX XX", **mpan(tuple(range(6))), dur=1, amp=1)
# d1 >> play("X", **mpan(expvar([0, 5.9], 4)))

print(tuple(range(6)))

d1.mpan(range(6))

Clock.bpm = 120

d2 >> play("x ", output=[4], pan=[-1])
d3 >> play(" X", output=[6], pan=[-1])
d1 >> play("  V", output=[2], pan=[1])
d4 >> play("v", output=[2], pan=[-1], dur=P[4/10, 3/10, 3/10] * 2)
# d5 >> play("x", output=[4], pan=[1], dur=[.4, .3, .3])
d6 >> play(P["X "].bubble(), output=[6], pan=[1])

d_all.sample = [0, 0, 1, 2, 0, 2, 2, 0, 1]

# c1 >> play("--(-- )", dur=[.4, .3, .3] * 2, **mpan([0, 2]), amp=4)
c2 >> play("(sss   )(   sss)", dur=cascara, **mpan(range(6)), amp=4)
c3 >> play("<T >< X>", sample=[0, 1, 2], **mpan([4, 5, 0, 1, 2, 3]))

c4 >> play(
    "w woo ",
    dur=[.5, .25, .25],
    amp=.3,
    sample=[2, (0, 2), (0, 1), (0, 2)],
    **mpan([0, 1, 2, 3, 4, 5])
)

d1 >> kit808("<x ><w ww w>", **span(linvar([1, 0], 4)))

p1 >> pluck([0, 2, 4], oct=3, amp=2, **mpan([0, 4]))
p2 >> pulse(
    [0, 1, -2, 4], oct=4, amp=2, **mpan([2, 3, 5]), dur=[.4, .3, .3] * 2
)

p3 >> bass(
    [0, 0, 1, 2, 0, 4],
    dur=PSum(3, 5),
    oct=[5, 6, 4],
    amp=1,
    **mpan(var(range(6), 8)),
    scale=Scale.minor
)

p3 >> crubass(
    [0, 0, 1, 2, 0, 4],
    dur=PSum(3, 5),
    oct=[2, 3, 3],
    amp=1,
    scale=Scale.minor,
    root=var([0, 2, -5], 16),
    # **span(0),
    # **span(linvar([0, 5.9], [1,0]), .8),
    # **span(linvar([0, 5.9], [8,0]), .8),
    # sur_y=1.5 * (yvar([0, 360], [8, 0]) - .15),
    # sur_x=1.5 * (xvar([0, 360], [8, 0]) - .15),
    # sur_y=yvar([0, 360], [8, 0])/5 + .5,
    # sur_x=xvar([0, 360], [8, 0])/5 + .5,
    # sur_x=.2 * (yvar([0, 360], [8, 0]) + 2)
    # sur_y=yvar([0, 360], [8, 0]),
    # sur_x=xvar([0, 360], [8, 0])
).span(linvar([0, 5.9], [8, 0]))

p2 >> marimba([0, 2, 4])

print(span(5))

# Clock.bpm = 140
Clock.bpm = 160

pi2 = 3.1416/2

m1 >> marimba(
    [0, 2, 4, 1, -2],
    oct=3,
    dur=cascara * 2,
    sur_y=expvar([.4, 1], 4),
    # sur_y=.5,
    # sur_x=.5,
    sur_x=linvar([0, 1], 7)
)

m2 >> marimba(
    [0, 2, 4, 1, -2],
    oct=4,
    dur=clave23 * 2,
)

k1 >> play("<x x><X  XX>", **mpan(PRand(0, 5)[:77]), sample=PRand(0, 3)[:13])
# k1 >> play("<x ><X >", **mpan(PRand(0, 5)[:17]), sample=PRand(0, 3)[:13])

d4 >> play(
    zipvar(
        [
            ('xxo[-o][-o]xo[-o]', 15),
            ('[oo]x', 1),
            ('xxo[-o][-o]xo[-o]', 14),
            ('[xx][ox]', 2),
            ('xxo[-o][-o]xo[-o]', 14),
            ('<ooxo>< = =>', 2),
            ('xxo[-o][-o]xo[-o]', 12),
            (' ', 4),
        ]
    ),
    formant=sinvar([0, 6], 16),
    amp=var([2, 0], [24, 8]),
    **mpan(linvar(range(6), 1)),
    # **mpan((0, 4)),
)

p1 >> loop(
    "foxdot",
    0,
    sdb=0,
    # dur=2,
    # dur=cascara,
    dur=PDur(3, 8) | [0.5, 1.5],
    # pshift=(0, 0.1),
    formant=sinvar([0, 6], 16),
    # formant=var([0, 4], [12, 4]),
    **mpan(range(6))
)

t1 >> play("Xo", dur=P[.4, .3, .3] * 2, output=4, pan=[-1, 1])
t2 >> play("w", dur=1, output=[2, 4], amp=.6)
