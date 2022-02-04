from fysom import Fysom
from pprint import pprint
import re
class MusicStateMachine:
    def __init__(self, events, max_time_count=512, max_transition_count=128):
        self.max_transition_count = max_transition_count
        self.max_time_count = max_time_count
        self.init, self.events, self.init_pattern = str(events[0][1]), events[1:], events[0][1]
        self.events = self._populate_triggers(self.events)
        self.time_counter = 0
        self._split_roundtrips_events()
        self.fsm_events = [{'name': 'event' + str(i), 'src': event[0], 'dst': event[1], 'trigger': event[2], 'pattern': event[3] } for i,event in enumerate(self.events)]
        self.fsm_states = [self.init]
        self.patterns = [events[0][1]] + [event['pattern'] for event in self.fsm_events]
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
                forth = (str(event[0]), str(event[1]), forth_trigger, event[0])
                # preceding_ev_src = self.init if i==0 or (self.events[i-1][0] == "*" and i==1) else self.events[i-2][1]
                # back_dst = event[0] if event[0] not in ["*",""] else preceding_ev_src
                # print(back_dst)
                if event[0] != '*':
                    back = (str(event[1]), str(event[0]), back_trigger, event[1])
                    res += [forth, back]
                else:
                    backs = [(str(event[1]), str(self.init), back_trigger, event[1])]
                    all_other_back_patterns = [self.init]
                    for ev in self.events:
                        if ev[0] != "*" and ev[0] not in all_other_back_patterns:
                            backs.append((str(event[1]), str(ev[0]), back_trigger, event[1]))
                            all_other_back_patterns.append(ev[0])
                    res += [forth] + backs
            else:
                res.append(event)
        self.events = res
    def _populate_triggers(self, event_list):
        res = [(event[0], event[1], MusicStateTrigger(expression=event[2])) for event in event_list]
        return res
    def _get_triggerable_transitions(self):
        return triggerable_events
    def generate_pvar(self):
        pvar_patterns = [self.init_pattern]
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
            event_to_trigger = events_matching_current_time[-1] # last event has priority
            self.fsm.trigger(event_to_trigger['name'])
            current_pattern = [pattern for pattern in self.patterns if str(pattern) == self.fsm.current][0]
            pvar_patterns.append(current_pattern)
            pvar_transition_times.append(t)
        self.pvar_patterns = pvar_patterns
        self.pvar_durations = [pvar_transition_times[i+1]-pvar_transition_times[i] for i in range(len(pvar_transition_times)-1)] if len(pvar_transition_times) > 1 else [16]
        self.pvar = Pvar(self.pvar_patterns, self.pvar_durations)
    def show_pvar(self):
        pprint([(self.pvar_patterns[i],self.pvar_durations[i]) for i in range(len(self.pvar_durations))])
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
msm = MusicStateMachine
def delay(config=None, vol=None, time=None, feedback=None, pan=None, dry=None):
    delay_base = { "delay_vol": 0, "delay_time": .5, "delay_feedback": .5, "delay_pan": .5, "delay_dry": 1 }
    if config and 'var' in config:
        dur = int(config[3:])
        vol = sinvar([0,.6],dur)
        time = 1 / (Clock.bpm / 60) # synchro delay time with current bpm
    vol = vol if vol is not None else delay_base["delay_vol"]
    time = time if time is not None else delay_base["delay_time"]
    feedback = feedback if feedback is not None else delay_base["delay_feedback"]
    pan = pan if pan is not None else delay_base["delay_pan"]
    dry = dry if dry is not None else delay_base["delay_dry"]
    return { "delay_vol": vol, "delay_time": time, "delay_feedback": feedback, "delay_pan": pan, "delay_dry": dry}
def lpf(freq, low_vol=0):
    return { "eq_gainlo": low_vol, "eq_freqlo": freq }
# b1 >> crubass(base1var([1,0],[6,2,7,1]), **delay(vol=1, pan=.5,dry=0))

import live
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
ab = SmartSet(Clock, set)

mixer = Instruc(smart_track=ab.mixer, midi_channel=-1, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kitcuba = Instruc(smart_track=ab.kitcuba, midi_channel=1, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kitdnb = Instruc(smart_track=ab.kitcuba, midi_channel=2, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kit808 = Instruc(smart_track=ab.kitdatai, midi_channel=3, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
kicker = Instruc(smart_track=ab.kicker, midi_channel=4, scale=Scale.chromatic, oct=3).out
kitdatai = Instruc(smart_track=ab.kitdatai, midi_channel=5, scale=Scale.chromatic, oct=3, midi_map="stdrum").out
ubass = Instruc(smart_track=ab.ubass, midi_channel=6, oct=4, scale=Scale.major).out
crubass = Instruc(smart_track=ab.crubass, midi_channel=7, oct=4, scale=Scale.major).out
strings = Instruc(smart_track=ab.strings, midi_channel=8, oct=5, scale=Scale.major).out
owstrings = Instruc(smart_track=ab.owstrings, midi_channel=9, oct=5, scale=Scale.major).out
balafon = Instruc(smart_track=ab.balafon, midi_channel=10, oct=6, scale=Scale.major).out
bells = Instruc(smart_track=ab.bells, midi_channel=11, oct=6, scale=Scale.major).out
kora = Instruc(smart_track=ab.bells, midi_channel=12, oct=6, scale=Scale.major).out
