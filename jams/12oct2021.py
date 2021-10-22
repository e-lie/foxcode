Clock.clear()


set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
Clock.midi_nudge = -0.08
mixer_track = set.tracks[0]
supercollider_track = set.tracks[1]
dj_mastering = mixer_track.devices[1]
eq_low = dj_mastering.parameters[1]

# kit808 = Instruc(1, 3, Clock)

street_bell = Instruc(1, 5, Clock)

p1 >> street_bell.init([0,3], dur=PDur(3,8), oct=4).every(3, "offadd", 2)

kickk = Instruc(2, 5, Clock)

k1 >> kickk.init([0])

bass = Instruc(2, 5, Clock)
pads = Instruc(3, 5, Clock)


p1 >> bass1.init(PWalk(8)[:30], dur=PDur(8,8))


b1 >> bass([0,4,5], dur=[4/10, 3/10, 3/10])

d1 >> play("<X o[  ][ o][  ]o[Xo]><- - - - ><  p  p  >")

d3 >> play(tps("8[x--1[-x]]"), dur=1/2)

d2 >> play(tps("2[-   -  -  ]")).

da_roda =

gnawa = [4/10, 3/10, 3/10] # Rhythm marocain traditionnel

d3 >> play("<x ><--(---x)>", dur=gnawa, sample=2, amp=[1,.5,.5])

d3 >> play("<x ><--(---x)>", dur=gnawa, sample=2, amp=[1,.5,.5])

d2 >> play("(ooox)(   [---])", sample=3, amp=.8)




d3 >> play("xtt", dur=1/3)


d2 >> play(tps("2[-   - - ]"), dur=1/2)

d2 >> play(tps("4[p  p  p  ]"), dur=1)


d3 >> play("X-")

set_param(eq_low, 1.0)
