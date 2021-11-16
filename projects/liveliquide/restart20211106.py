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
from pprint import pprint
import re
class MusicStateMachine:
    def __init__(self, events, max_time_count=512, max_transition_count=128):
        self.max_transition_count = max_transition_count
        self.max_time_count = max_time_count
        self.init, self.events = events[0][1], self._populate_trigger_objects(events[1:])
        self.time_counter = 0
        self._split_roundtrips_events()
        self.fsm_events = [{'name': 'event' + str(i), 'src': event[0], 'dst': event[1], 'trigger': event[2]} for i,event in enumerate(self.events)]
        self.fsm_states = [self.init]
        self.current_state = self.init
        self.preceding_state = self.init
        for event in self.fsm_events:
            if event["dst"] not in self.fsm_states:
                self.fsm_states.append(event["dst"])
        self.fsm = Fysom(initial=self.init,
                         events=self.fsm_events)
        self.generate_pvar()
    def _split_roundtrips_events(self):
        res = []
        for i, event in enumerate(self.events):
            if event[2].roundtrip: # split element in two events forth and back
                forth_trigger, back_trigger = event[2].split_roundtrip_trigger()
                forth = (event[0], event[1], forth_trigger)
                # preceding_ev_src = self.init if i==0 or (self.events[i-1][0] == "*" and i==1) else self.events[i-2][1]
                # back_dst = event[0] if event[0] not in ["*",""] else preceding_ev_src
                # print(back_dst)
                if event[0] != '*':
                    back = (event[1], event[0], back_trigger)
                    res += [forth, back]
                else:
                    backs = [(event[1], self.init, back_trigger)]
                    all_other_back_patterns = [self.init]
                    for ev in self.events:
                        if ev[0] != "*" and ev[0] not in all_other_back_patterns:
                            backs.append((event[1], ev[0], back_trigger))
                            all_other_back_patterns.append(ev[0])
                    res += [forth] + backs
            else:
                res.append(event)
        self.events = res
    def _populate_trigger_objects(self, event_list):
        return [(event[0], event[1], MusicStateTrigger(expression=event[2])) for event in event_list]
    def _get_triggerable_transitions(self):
        return triggerable_events
    def generate_pvar(self):
        pvar_patterns = [self.init]
        pvar_transition_times = [0]
        transition_count = 0
        visited_state_count = 1
        for t in range(1, self.max_time_count): # only works with int number of beats for now
            # stop conditions
            max_transition_reached = transition_count >= self.max_transition_count
            init_and_all_state_visited = self.fsm.current == self.init and visited_state_count >= len(self.fsm_states)
            # infinite_state_reached = self.current_trigger.is_infinite()
            if max_transition_reached or init_and_all_state_visited:
                break
            triggerable_events = filter(lambda ev: self.fsm.can(ev['name']), self.fsm_events)
            events_matching_current_time = list(filter(lambda ev: ev['trigger'].match_clock(t), triggerable_events))
            if not events_matching_current_time:
                continue # go to next time point to explore
            event_to_trigger = events_matching_current_time[-1]
            self.fsm.trigger(event_to_trigger['name'])
            pvar_patterns.append(self.fsm.current)
            pvar_transition_times.append(t)
        self.pvar_patterns = pvar_patterns
        self.pvar_durations = [pvar_transition_times[i+1]-pvar_transition_times[i] for i in range(len(pvar_transition_times)-1)] if len(pvar_transition_times) > 1 else [16]
        self.pvar = Pvar(self.pvar_patterns, self.pvar_durations)
    def show_pvar(self):
        pprint([(testounet.pvar_patterns[i],testounet.pvar_durations[i]) for i in range(len(testounet.pvar_durations))])
    def show_events(self):
        pprint(self.events)
class MusicStateTrigger:
    def __init__(self, expression=None, modulo=None, offset=0, roundtrip_after=None):
        if modulo is not None:
            self.modulo = int(modulo) if modulo is not None else None
            self.offset = float(offset)
            self.roundtrip_after = float(roundtrip_after) if roundtrip_after is not None else None
            self.roundtrip = isinstance(self.roundtrip_after, float) and self.roundtrip_after > 0
        elif expression is not None:
            modulo, offset_direction, offset, roundtrip_after = re.match("^mod(\d+(?:\.\d+)?)([ab]?)(\d+(?:\.\d+)?)?r?(\d+(?:\.\d+)?)?", expression).groups()
            offset = 0.0 if offset is None else offset
            self.modulo = int(modulo)
            self.roundtrip_after = float(roundtrip_after) if roundtrip_after is not None else None
            self.offset = -float(offset) if offset_direction == 'b' else float(offset)
            self.roundtrip = isinstance(self.roundtrip_after, float) and self.roundtrip_after > 0
        else:
            raise TypeError()
    def split_roundtrip_trigger(self):
        return MusicStateTrigger(modulo=self.modulo, offset=self.offset), MusicStateTrigger(modulo=self.modulo, offset=self.offset + self.roundtrip_after)
    def match_clock(self, clock_time):
        if self.offset >= 0:
            match = clock_time % self.modulo == self.offset
        else:
            match = clock_time % self.modulo == self.offset + self.modulo
        return match
    def __repr__(self):
        return "<MusicStateTrigger: {} {} {}>".format(self.modulo, self.offset, self.roundtrip_after)

testounet = MusicStateMachine([
    ('init','xxo[-o][-o]xo[-o]'),
    ('xxo[-o][-o]xo[-o]','xxo[-o]    ', 'mod16b4r4'),
    ('*','o o    [oooo]','mod16r4'),
    ('*','x-o--xo-','mod32r8'),
    ('*','x-o-','mod64r8'),
])
testounet.show_events()

p2 >> play(Pvar(testounet.pvar_patterns, testounet.pvar_durations, start=Clock.mod(4)), sample=0, dur=1/2)

p2 >> play("Xo")


################################################################

# Linked pitch+dur using functions and unpacking

def linkedpd():
    return {'pitch' : P[0,1,2], 'dur': gnawa }

p1 >> play(**linkedpd())
