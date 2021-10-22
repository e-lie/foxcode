from functools import partial

Clock.clear()


set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
Clock.midi_nudge = -0.08
mixer_track = set.tracks[0]
supercollider_track = set.tracks[1]
dj_mastering = mixer_track.devices[0]
eq_low = dj_mastering.parameters[1]

marimba = Instruc(1, 5, Clock)
basse = Instruc(2, 3, Clock)

triolet = [1/3, 1/3, 1/3]
gnawa = [4/10, 3/10, 3/10] # rythme marocain traditionnel
binaire = [1/2, 1/4, 1/4]

d4 >> play("ooo", sample=0, dur=Pvar(morphing(binaire, triolet, step=10), 2))

playg = partial(play, dur=gnawa)

d1 >> playg("---")

d1 >> play("---", dur=gnawa, sample=2, amp=[1,.5,.5])

d1 >> play("<x ><--->", dur=gnawa, sample=2, amp=[1,.5,.5])
d1 >> play("<x ><--(---x)>", dur=gnawa, sample=2, amp=[1,.5,.5])
d1 >> play("<(Xx) ><--(---x)>", dur=gnawa, sample=2, amp=[1,.5,.5])

d2 >> play("o ", sample=3, amp=.8)
d2 >> play("(ooox) ", sample=3, amp=.8)
d2 >> play("(ooox)(   [---])", sample=3, amp=.8)

d3 >> play("(XxX x X ) ", sample=2)

m1 >> basse.init(PWalk()[:100], scale=Scale.minorPentatonic, amp=PWhite(0,1)[:100]).stop()

m2 >> marimba.init(PWalk(step=2)[:100], oct=4, scale=Scale.minorPentatonic, dur=Pvar(morphing(binaire, triolet, step=10)), amp=PWhite(0.3,1)[:100])



da_roda = P[0.25, 0.22, 0.25, 0.28] * 1.5

r1 >> play("----", dur=da_roda, amp=[1, 1, 0.2, 1])

r2 >> marimba.init([7,0,0,7,7,0,0,0], dur=da_roda, amp=[1, .8, .8, .8], oct=7)

set_param(eq_low, 0.0)
