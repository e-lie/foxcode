r1 >> play(
    # "o",
    "<ooo oo oooo ><v >",
    # "<o><X >",
    # amp=[.8,.9,1.1],
    amp=Pvar([[.8, .9, 1.1], 0], [24, 8]),
    sample=var([0, 2, 1, 3], [8, 3, 5]),
    dur=var([1/3, .25, 1], [8, 3, 5]),
    formant=0,
    rate=0.2,
    room=3,
    **mpan(range(6))
)

p1 >> fordrip([0, 0, 17]).span(linvar([0, 5.9], [8, 0]))

b1 >> accciddd([0, 2, 4], dur=4, oct=3).span(rotrand1)

################################################################

wh >> whirl(
    feedback=.9, depth=linvar([0, 1], 17), whirl_delay=linvar([0, .1], 8)
)
sv >> sverb(mix=.5)

k1 >> play(
    "<o><v  ><[ooo]  (wV) >",
    #dur=1,
    formant=linvar([0, 2], 17)
).mpan(range(6))
tt >> play("TT TTT ", dur=cascara).mpan(range(6))
t2 >> play("dd wdd ", dur=clave23, sample=range(4)).mpan(range(6))

################################################################

k1 >> kicker("AA A AAA", dur=cascara, amp=PWhite(.6, 1.2)[:17])
k2 >> kicker("ddd dddd ", dur=clave23, amp=PWhite(.6, 1.2)[:17])

k3.span(rotrand1)

k3 >> kicker("jjj", dur=cubalet, amp=PWhite(.6, 1.2)[:17])

k3.tex = .6
k3.lpf_freq = 400
