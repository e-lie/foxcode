import live
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
ab = SmartSet(Clock, set)
kitcuba = Instruc(smart_track=ab.kitcuba, midi_channel=1, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kicker = Instruc(smart_track=ab.kicker, midi_channel=2, scale=Scale.chromatic, oct=3).out
kitdatai = Instruc(smart_track=ab.kitdatai, midi_channel=3, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kit808 = Instruc(smart_track=ab.kitdatai, midi_channel=1, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
ubass = Instruc(smart_track=ab.ubass, midi_channel=4, oct=4, scale=Scale.major).out
crubass = Instruc(smart_track=ab.crubass, midi_channel=5, oct=4, scale=Scale.major).out
strings = Instruc(smart_track=ab.strings, midi_channel=6, oct=5, scale=Scale.major).out
owstrings = Instruc(smart_track=ab.owstrings, midi_channel=7, oct=5, scale=Scale.major).out
balafon = Instruc(smart_track=ab.balafon, midi_channel=8, oct=6, scale=Scale.major).out
bells = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out
kora = Instruc(smart_track=ab.bells, midi_channel=9, oct=6, scale=Scale.major).out

Clock.bpm = 120
Clock.midi_nudge = 0.29 # bpm 120

Clock.bpm = 130
Clock.midi_nudge = 0.22 # bpm 120

Clock.bpm = 140
Clock.midi_nudge = 0.19 # bpm 140

Clock.bpm = 160
Clock.midi_nudge = 0.16

################################################################

base1 = var([0,2,0,4],4)
root1 = var([0,4,2,0],16)

bin3 = P[1/2,1/4,1/4]
gnawa = P[4/10,3/10,3/10]
ter3 = P[1/3,1/3,1/3]

b1 >> crubass(base1, dur=PSum(3,2), oct=3, root=root1, scale=Scale.minor, vol=.9)

d1 >> kitcuba(PRand(range(20))[:32], dur=gnawa, amp=Pvar([[1,.5],0],[6,2]), pan=sinvar([1,-1],4), reverb_dry_wet=expvar([0,.8],8))

k1 >> kicker(1, dur=1, oct=3, amp=var([1,0],[12,4])).every(8, "stutter", 3)

s1 >> strings(base1, dur=2, oct=4, root=root1, scale=Scale.minor, vol=.8, amp=var([1,0], [12,4]), i_release=.8 )

k1.only()

################################################################

base2 = var([0,4,1,4,0,2,4,2],2)
root2 = var([0,6],16)
scale2 = Pvar([Scale.minor,Scale.major],32)

d1 >> play(" (---[oo])", sample=var([2,3,4],1), amp=.2)
k1 >> kicker([6,(4,12)], dur=1, oct=3, amp=var([1,0],[28,4])).every(16, "stutter", 2)

b1 >> crubass(base2, dur=PSum(5,3), oct=3, root=root2, scale=scale2, vol=.9, i_cutoff=sinvar([.3,1], 8), i_intensity=sinvar([.3,1], 32), i_wt_pos=sinvar([0,1], 8))
b2 >> ubass(base2, dur=PSum(5,3), amp=1, oct=3, root=root2, scale=scale2)


################################################################

# Example ramp

d1 >> play(" (---[oo])", dur=1/2, sample=var([2,3,4],1), amp=.5)
b1 >> crubass(base2, dur=PSum(5,3), oct=3, root=root2, scale=scale2, vol=.9, i_cutoff=.5, i_intensity=.5, i_wt_pos=.5)
b2 >> ubass(base2, dur=PSum(5,3), amp=1, oct=3, root=root2, scale=scale2)

ramp = linvar([0,1],[14,inf],start=Clock.mod(4))
ramp2 = linvar([.9,.6,1],[2,12,inf],start=Clock.mod(4))
d1 >> kitdatai("[***]", amp=ramp,dur=1/2)
b1 >> crubass(base2, dur=PSum(5,3), oct=3, root=root2, scale=scale2,
              amp=ramp2,
              i_cutoff=ramp,
              i_intensity=ramp,
              i_wt_pos=ramp)

d1 >> kicker([6,(4,12)], dur=1, oct=3, amp=var([1,0],[28,4])).every(16, "stutter", 2)


################################################################

# Playing with bells, modes and octaves
# I Ionian (diatonic major) -> Scale.major
# II Dorian
# III Phrygian -> root = 4 = III
# IV Lydian -> root = 5 = IV
# V Mixolydian
# VI Aeolian
# VII Locrian

moct = var([4,4.5,5], 16) # var doesn't with ableton instruments -> bug to fix
p1 >> bell(Pvar([Scale.major, Scale.lydian, Scale.phrygian],8), oct=moct, dur=gnawa, root=0, amp=var([.8,0,.8],[16,4,12])).every(7,"stutter",3)
p2 >> bell([P+(0,2,4,6)], dur=4, sus=4, oct=moct, root=var([0,5,4],8), scale=Scale.major, amp=var([.8,0,.8],[12,4,16]))
k1 >> kicker(1, dur=1, oct=3, amp=var([1,0],[28,4])).every(8, "stutter", 3)

################################################################

# Jungle !!! 1

b1 >> crubass(base2, dur=PSum(5,3), oct=2, root=root2, scale=scale2, vol=.9, i_cutoff=.5, i_intensity=.5, i_wt_pos=.5)
b2 >> ubass(base2, dur=PSum(5,3), amp=1, oct=3.5, root=root2, scale=scale2)

d1 >> play(Pvar(["xxo[-o][-o]xo[-o]", "x-o--xo-"], [24,8], start=Clock.mod(4)), dur=1/2)
# d1 >> play(Pvar(["XXO[-O][-O]XO[-O]", "X-O--XO-"], [24,8], start=Clock.mod(4)))

tt >> play("V", sample=var([1,2,3],1))

d1 >> kitdatai(Pvar(["xxo[-o][-o]xo[-o]", "x-o--xo-"], [24,8], start=Clock.mod(4)), dur=1/2)
d2 >> kitdatai("c   [ (cs)]", dur=1/2)
d3 >> play("X ", sample=2)

################################################################

# variable patterns from finite state machine ?

from fysom import Fysom
import re

fsm = Fysom(initial='base',
          events=[
              ('tobreak1',  'base',  'break1'),
              ('tobreak2',  'base',  'break2'),
              ('rebase', ['break1','break2'], 'base'),
              ])

print(fsm.current)
fsm.tobreak1()
fsm.rebase()

patternism = [
    ('init','xxo[-o][-o]xo[-o]'),
    ('xxo[-o][-o]xo[-o]','x-o--xo-','mod16b4r4'),
    ('xxo[-o][-o]xo[-o]','x-o-','mod64b4r8')
]

class MusicStateMachine:
    def __init__(self, events):
        self.init, self.events = events[0][1], self._populate_trigger_objects(events[1:])
        self._split_roundtrips_events()
        self.fsm = Fysom(initial=self.init,
                         events=[{'name': 'event' + str(i), 'src': event[0],  'dst': event[1]} for i,event in enumerate(self.events)])
    def _split_roundtrips_events(self):
        res = []
        for event in self.events:
            if event[2].roundtrip: # split element in two events forth and back
                forth_trigger, back_trigger = event[2].split_roundtrip_trigger()
                forth = (event[0], event[1], forth_trigger)
                back = (event[1], event[0], back_trigger)
                res += [forth, back]
            else:
                res.append(event)
    def _populate_trigger_objects(self, event_list):
        return [(event[0], event[1], MusicStateTrigger(expression=event[2])) for event in event_list]
class MusicStateTrigger:
    def __init__(self, expression=None, modulo=None, offset=None, roundtrip_after=None):
        if modulo is not None:
            self.modulo = float(modulo) if modulo is not None else None
            self.offset = float(offset) if offset is not None else None
            self.roundtrip_after = float(roundtrip_after) if roundtrip_after is not None else None
            self.roundtrip = isinstance(self.roundtrip_after, float) and self.roundtrip_after > 0
        elif expression is not None:
            modulo, offset_direction, offset, roundtrip_after = re.match("^mod(\d+(?:\.\d+)?)([ab]?)(\d+(?:\.\d+)?)?r?(\d+(?:\.\d+)?)?", expression).groups()
            self.modulo = float(modulo)
            self.roundtrip_after = float(roundtrip_after) if roundtrip_after is not None else None
            if offset:
                self.offset = -float(offset) if offset_direction == 'b' else float(offset)
            else:
                self.offset = None
            self.roundtrip = isinstance(self.roundtrip_after, float) and self.roundtrip_after > 0
        else:
            raise TypeError()
    def split_roundtrip_trigger(self):
        return MusicStateTrigger(modulo=self.modulo, offset=self.offset), MusicStateTrigger(modulo=self.modulo, offset=self.offset + self.roundtrip_after)

testounet = MusicStateMachine(patternism)

print(testounet.events[1][2].roundtrip)


################################################################

# Linked pitch+dur using functions and unpacking

def linkedpd():
    return {'pitch' : P[0,1,2], 'dur': gnawa }

p1 >> play(**linkedpd())
