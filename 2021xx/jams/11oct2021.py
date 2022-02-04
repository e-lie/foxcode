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
bass = Instruc(2, 5, Clock)
pads = Instruc(3, 5, Clock)


p1 >> street_bell.init(PWalk(8)[:30], dur=PDur(8,8))

p1 >> street_bell.init([0,3], dur=PDur(3,8)).every(3, "offadd", 2)

b1 >> bass([0,4,5], dur=[4/10, 3/10, 3/10])

d1 >> play("<X o[  ][ o][  ]o[Xo]><- - - - ><  p  p  >")


set_param(eq_low, 1.0)