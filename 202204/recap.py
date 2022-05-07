from FoxDot.preset import *

change_bpm(120, True)
mi >> mixer()
sc >> sc()

wh >> whirl(whirl_feedback=linvar([.8, .95], 17))
wh.whirl_feedback = 0

k1 >> kicker(
    "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQ",
    oct=3,
    sample=var([0, 1, 2], 8),
    amp=2
).span(linvar([0, 5.9], [8, 0]), .5)

m1.solo()

k1.dur = cubalet
k1.sverb = .3
k1.whirl = .5

b1 >> crubass([2, 4, 6], oct=2, dur=cubalet * 2,
              root=[2, 4, 0, -5]).span(linvar([0, 5.9], [16, 0]))

m1 >> marimba([2, 4, 6], oct=3, dur=cubalet,
              root=[2, 4, 0, -5]).span(linvar([0, 5.9], [16, 0]))

m1.amp = linvar([.3, 1], 9)
m2 >> marimba([2], oct=2, dur=.5, root=[2, 4, 0, -5], amp=linvar([0, 1], 7)
             ).span(linvar([0, 5.9], [16, 0])) + (0, 2, 3)

s1 >> crazykit("ss( s)", dur=cubalet).span(var([0, 2, 4], 7))
