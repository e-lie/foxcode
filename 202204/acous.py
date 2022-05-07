from FoxDot.preset import *

change_bpm(110)
sc >> supercollider(0, whirl=.6, mixer=0)
mi >> mixer()
wh >> whirl(whirl_feedback=sinvar([.7, .9], 8))
sv >> sverb()
de >> delay()
tx >> tex()
sh >> shimoct()

k1 >> play("x(   X)").mpan(PRand(0, 5)[:17])

k1 >> play("o", dur=1).mpan(range(6))

wh.whirl_feedback = 0

k1 >> play("<V><(     [X[xv]])>", sample=0, dur=1).mpan([0, 0, 0, 3, 3, 3])
k1.dur = gnawa * 2

d1 >> play("-- ", dur=cubalet, amp=2).mpan(2)
d1.sverb = .5

d2 >> play("TTT ", dur=.5).mpan([4, 5])

m1 >> marimba([2, 4, 6], oct=3, dur=cubalet,
              root=[2, 4, 0, -5]).span(linvar([0, 5.9], [16, 0]))
