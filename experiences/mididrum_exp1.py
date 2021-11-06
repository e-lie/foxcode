from .Custom import *
Clock.bpm=92
Clock.midi_nudge=0.29
lowcase = list(range(97,123))
upcase = list(range(65,91))
base_midi_map = {'default': 2, ' ': -1}
for i in range(52):
    if i % 2 == 0:
        base_midi_map[chr(lowcase[i//2])] = i
    else:
        base_midi_map[chr(upcase[i//2])] = i
gnawa = P[4/10,3/10,3/10]
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
# fk_reso = SmartDevice(set.tracks[4].devices[1])
ab = SmartSet(set)
kit909 = InstrumentFacade(smart_track=ab.kit909, midi_channel=2, oct=3).out

d1 >> kit909("abcd", dur=1/2, pan=sinvar([1,-1],4), reso_dw=expvar([.2,.6],12))

ab.kit909.resoberlin.dry_wet = expvar([0,.5],[3,1])
ab.kit909.resoberlin.color = sinvar([0,1],[3,4])
ab.kit909.resoberlin.width = sinvar([0,1],[5,4])

ab.kit909.resoberlin.dry_wet = 0.5

ab.kit909.pan = sinvar([-1,1],[4,4])

ab.pan = 0

d1 >> kit909("a ")

d1 >> drumm.init("<a ><BBB>", oct=3, dur=gnawa, midi_map=base_midi_map)
d2 >> drumm2.init("<(abbb) >", oct=3, dur=1/2, midi_map=base_midi_map)

d1 >> drumm.init("(aaa[aa])(dddH)", oct=3, dur=1/2, sus=1/2, midi_map=base_midi_map)
d2 >> drumm2.init("<bb>", oct=3, dur=gnawa, midi_map=base_midi_map)

d3 >> play("X(   [---])", sample=2)

print(type(ab.kit909.__track))
